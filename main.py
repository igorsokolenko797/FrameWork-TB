import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.model import async_main


async def main():
    await async_main()
    bot = Bot(token='7158466452:AAEa8MQCMBtRG9ozzZRBPH6EQbydct_2vg8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')