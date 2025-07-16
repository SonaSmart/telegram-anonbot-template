# Telegram Anonymous Bot

Этот бот принимает анонимные сообщения и пересылает их администратору.

## Как запустить на Render:
- Перейди на https://render.com
- Создай Web Service, подключи GitHub
- Добавь переменные окружения:
  - BOT_TOKEN = твой_токен
  - ADMIN_ID = твой Telegram ID
- Build command: pip install -r requirements.txt
- Start command: python main.py
