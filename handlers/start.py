from aiogram import Router, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    name = html.bold(message.from_user.full_name)
    await message.answer(
        f"Привет, {name}!\n"
        "Я бот-заметки на aiogram.\n\n"
        "/add текст — сохранить заметку\n"
        "/list — показать заметки\n"
        "/help — справка"
    )


@router.message(Command("help"))
async def command_help(message: Message) -> None:
    await message.answer(
        "Команды:\n"
        "/start — приветствие\n"
        "/add купить молоко — добавить заметку\n"
        "/list — список заметок\n"
        "/help — эта справка"
    )
