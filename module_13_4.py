from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = ''
bot = Bot(token=api)
disp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@disp.message_handler(commands=['start'])
async def start_message(message):
    print('"start_message" перехватил сообщение')
    await message.answer('Привет! Я бот помогающий твоему здоровью')


@disp.message_handler(text=['Calories', 'Калории', 'Каллории'])
async def set_age(message):
    await message.answer('Введите свой возраст')
    await UserState.age.set()


@disp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer('Введите свой рост')
    await UserState.growth.set()


@disp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    await message.answer('Введите свой вес')
    await UserState.weight.set()


@disp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    await message.answer(f'Необходимая норма каллорий для Вас '
                         f'{10*float(data["weight"])+6.25*float(data["growth"])-5*float(data["age"]) - 161}')
    await state.finish()


@disp.message_handler()
async def all_message(message):
    print('"all_message" перехватил сообщение')
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)