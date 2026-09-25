# Telegram-бот на aiogram

Простой бот-заметки. Сделан по [официальному примеру echo_bot](https://github.com/aiogram/aiogram/blob/dev-3.x/examples/echo_bot.py): `Bot`, `Dispatcher`, роутеры и хендлеры команд.

## Команды

- `/start` — приветствие
- `/help` — справка
- `/add текст` — сохранить заметку
- `/list` — показать заметки

Сейчас заметки хранятся в памяти процесса. Следующий шаг — таблица SQL (`users` + `notes`).

## Запуск

1. Создай бота в [@BotFather](https://t.me/BotFather) и скопируй токен.
2. Установи зависимости:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Запусти:

```bash
export BOT_TOKEN="твой_токен"
python main.py
```

## Структура

```
main.py              # точка входа, polling
handlers/start.py    # /start и /help
handlers/notes.py    # /add и /list
storage.py           # временное хранилище (потом SQL)
```
