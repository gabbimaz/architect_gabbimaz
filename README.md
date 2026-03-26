# Telegram бот: кнопка "Архітектор" -> посилання на файл

Цей бот після натискання на кнопку **«Архітектор»** надсилає посилання на файл у чат.

## 1) Отримай токен у BotFather
1. Відкрий Telegram і знайди `@BotFather`.
2. Виконай команду `/newbot`.
3. Задай ім'я і username бота.
4. Скопіюй токен (рядок на кшталт `123456:ABC-DEF...`).

## 2) Встановлення
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3) Налаштуй `.env`
У проєкті вже є файл `.env`. Відкрий його і встав свій токен:

```env
BOT_TOKEN=PASTE_YOUR_BOTFATHER_TOKEN_HERE
FILE_URL=https://drive.google.com/file/d/1CNmTiUVRW8dyHEOMikiVusVfoT3JzJN2/view?usp=sharing
```

- `BOT_TOKEN` — токен із BotFather.
- `FILE_URL` — посилання на файл (за замовчуванням уже вставлене потрібне Google Drive посилання).

## 4) Запуск
```bash
python bot.py
```

## 5) Використання
1. Відкрий свого бота в Telegram.
2. Надішли `/start`.
3. Натисни кнопку **«Архітектор»**.
4. Бот надішле посилання на файл.

## Важливо
- Не публікуй реальний токен у публічних репозиторіях.
