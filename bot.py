import logging
import os

from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

ARCHITECT_CALLBACK = "architect_link"
DEFAULT_FILE_URL = (
    "https://drive.google.com/file/d/1CNmTiUVRW8dyHEOMikiVusVfoT3JzJN2/view?usp=sharing"
)
FILE_URL = os.getenv("FILE_URL", DEFAULT_FILE_URL)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Надсилає кнопку 'Архітектор'."""
    keyboard = [[InlineKeyboardButton("Архітектор", callback_data=ARCHITECT_CALLBACK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Натисни кнопку, щоб отримати посилання на файл:",
        reply_markup=reply_markup,
    )


async def architect_button_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Відправляє посилання після натискання на кнопку."""
    query = update.callback_query
    await query.answer()

    await query.message.reply_text(f"Ось посилання на файл:\n{FILE_URL}")


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError(
            "Не знайдено BOT_TOKEN. Додай токен бота в .env або змінні оточення."
        )

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        CallbackQueryHandler(architect_button_handler, pattern=f"^{ARCHITECT_CALLBACK}$")
    )

    logger.info("Бот запущений...")
    application.run_polling()


if __name__ == "__main__":
    main()
