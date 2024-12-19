from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import initiate_db, add_product, get_all_products, add_user, is_included


api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Основная клавиатура Reply
main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Регистрация')],
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Купить')
        ]
    ],
    resize_keyboard=True
)

initiate_db()
add_product('AEVIT', 100, 'AEVIT_PRO', 'AE.jpg')
add_product('ASKORBINKA', 200, None, 'ASK.jpg')
add_product('COMPLIVIT', 300, "don't forget", 'COM.jpg')
add_product('GEMATOGEN', 400, None, 'GEM.jpg')

# Основная клавиатура Inline
inl_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Формулы рассчёта', callback_data='formula')],
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calculate')]
    ]
)

# Клавиатура Inline для выбора приобретаемого продукта
buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='product_1', callback_data='product_buying')],
        [InlineKeyboardButton(text='product_2', callback_data='product_buying')],
        [InlineKeyboardButton(text='product_3', callback_data='product_buying')],
        [InlineKeyboardButton(text='product_4', callback_data='product_buying')]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands='start')
async def starter(msg):
    print('Bot started')
    await msg.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=main_kb)


@dp.message_handler(text='Информация')
async def inform(msg):
    print('Нажата кнопка "Информация"')
    await msg.answer('Пока что я могу только рассчитать каллории, необходимые тебе в состоянии покоя и '
                     'предложить приобрести товар')


@dp.message_handler(text='Рассчитать')
async def run_calc(msg):
    print('Нажата кнопка "Рассчитать"')
    await msg.answer('Выберите опцию:', reply_markup=inl_kb)


@dp.callback_query_handler(text='formula')
async def print_formula(call):
    print('Запрос формуры для рассчёта')
    await call.message.answer('BMR = 10 x вес(кг) + 6.25 x рост(см) − 5 x возраст(лет) − 161')
    await call.answer()


# Здесь блок регистрации пользователей
@dp.message_handler(text='Регистрация')
async def sing_up(msg):
    print('Сработала кнопка "Регистрация"')
    await msg.answer('Введите имя пользователя (только латинский алфавит)')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(msg, state):
    user = msg.text
    if is_included(user):
        await msg.answer('Пользователь существует, введите другое имя')
    else:
        await state.update_data(username=msg.text)
        await msg.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(msg, state):
    await state.update_data(email=msg.text)
    await msg.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(msg, state):
    await state.update_data(age=msg.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await msg.answer('Регистрация завершена! Добро пожаловать!')
    await state.finish()

# Здесь блок приобретения товара
@dp.message_handler(text='Купить')
async def get_buying_list(msg):
    product_lst = get_all_products()
    print('Нажата кнопка "Купить"')
    for product in product_lst:
        if product[-1] != 'None':
            with open(f'files/{product[-1]}', 'rb') as img:
                if product[1] != 'None':
                    await msg.answer_photo(img,
                                       f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')
                else:
                    await msg.answer_photo(img,
                                           f'Название: {product[0]}| Цена: {product[2]}')
        else:
            if product[1] != 'None':
                await msg.answer(f'Название: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')
            else:
                await msg.answer(f'Название: {product[0]}| Цена: {product[2]}')
    await msg.answer('Выберите продукт для покупки', reply_markup=buy_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    print('Выбор товара')
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


#  Здесь происходит действие кнопки "Рассчитать"
@dp.callback_query_handler(text='calculate')
async def set_age(call):
    print('Запускаем рассчёт каллорий')
    await call.message.answer('Введите свой возраст')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    await message.answer(f'Необходимая норма каллорий для Вас '
                         f'{10 * float(data["weight"]) + 6.25 * float(data["growth"]) - 5 * float(data["age"]) - 161}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('"all_message" перехватил сообщение')
    await message.answer('Введите команду /start, чтобы начать общение')
    await message.answer('Или выберите одну из доступных кнопок')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
