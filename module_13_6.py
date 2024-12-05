from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True
)

inl_kb = InlineKeyboardMarkup()
f_btn = InlineKeyboardButton(text='Формулы рассчёта', callback_data='formula')
calc_btn = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calculate')
inl_kb.add(calc_btn)
inl_kb.add(f_btn)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands='start')
async def starter(msg):
    print('Bot started')
    await msg.answer('Привет! Я бот помогающий твоему здоровью', reply_markup=main_kb)


@dp.message_handler(text='Информация')
async def inform(msg):
    print('Нажата кнопка "Информация"')
    await msg.answer('Пока что я могу только рассчитать каллории, необходимые тебе в состоянии покоя')


@dp.message_handler(text='Рассчитать')
async def run_calc(msg):
    print('Нажата кнопка "Рассчитать"')
    await msg.answer('Выберите опцию:', reply_markup=inl_kb)


@dp.callback_query_handler(text='formula')
async def print_formula(call):
    print('Запрос формуры для рассчёта')
    await call.message.answer('BMR = 10 x вес(кг) + 6.25 x рост(см) − 5 x возраст(лет) − 161')
    await call.answer()


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
                         f'{10*float(data["weight"])+6.25*float(data["growth"])-5*float(data["age"]) - 161}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print('"all_message" перехватил сообщение')
    await message.answer('Введите команду /start, чтобы начать общение')
    await message.answer('Или выберите одну из доступных кнопок')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
