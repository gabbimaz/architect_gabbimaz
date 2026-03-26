# Telegram бот: кнопка "Архітектор" -> PDF

Цей бот після натискання на кнопку **«Архітектор»** надсилає PDF-файл у чат.

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
PDF_PATH=architect.pdf
```

- `BOT_TOKEN` — токен із BotFather.
- `PDF_PATH` — шлях до PDF (можна абсолютний або відносний).

## 4) Підготуй PDF
- Поклади потрібний PDF у корінь проєкту з назвою `architect.pdf`,
  **або** зміни `PDF_PATH` у `.env`.

## 5) Запуск
```bash
python bot.py
```

## 6) Використання
1. Відкрий свого бота в Telegram.
2. Надішли `/start`.
3. Натисни кнопку **«Архітектор»**.
4. Бот надішле PDF-файл.

## Важливо
- Не публікуй реальний токен у публічних репозиторіях.
- Якщо файл не знайдено, бот повідомить про це у чаті.
