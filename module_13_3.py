from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = ''
bot = Bot(token=api)
disp = Dispatcher(bot, storage=MemoryStorage())


@disp.message_handler(commands=['start'])
async def start_message(message):
    print('"start_message" перехватил сообщение')
    await message.answer('Привет! Я бот помогающий твоему здоровью')


@disp.message_handler()
async def all_message(message):
    print('"all_message" перехватил сообщение')
    await message.answer('Введите команду /start, чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)
