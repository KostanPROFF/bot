#!venv/bin/python
import logging
from aiogram import Bot, Dispatcher, executor, types

# Объект бота
bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
