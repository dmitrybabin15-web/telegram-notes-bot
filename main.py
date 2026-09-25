import asyncio
import logging
import sys
from pathlib import Path
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import router

load_dotenv(Path(__file__).resolve().parent / ".env")
TOKEN = getenv("BOT_TOKEN")


async def main() -> None:
    if not TOKEN:
        raise RuntimeError("Set BOT_TOKEN (from @BotFather)")

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
