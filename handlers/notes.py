from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

from storage import add_note, list_notes

router = Router()


@router.message(Command("add"))
async def command_add(message: Message, command: CommandObject) -> None:
    text = (command.args or "").strip()
    if not text:
        await message.answer("Напиши так: /add купить молоко")
        return

    add_note(message.from_user.id, text)
    await message.answer(f"Сохранил: {text}")


@router.message(Command("list"))
async def command_list(message: Message) -> None:
    items = list_notes(message.from_user.id)
    if not items:
        await message.answer("Пока пусто. Добавь заметку: /add текст")
        return

    lines = "\n".join(f"{i}. {note}" for i, note in enumerate(items, start=1))
    await message.answer(f"Твои заметки:\n{lines}")
