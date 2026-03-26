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

ARCHITECT_CALLBACK = "architect_pdf"
FILE_URL = os.getenv("FILE_URL", "")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("Архітектор", callback_data=ARCHITECT_CALLBACK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Натисни кнопку, щоб отримати PDF файл:",
        reply_markup=reply_markup,
    )


async def architect_button_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    query = update.callback_query
    await query.answer()

    if not FILE_URL:
        await query.message.reply_text("Посилання не налаштовано. Додай FILE_URL у .env")
        return

    await query.message.reply_text(
        f"Ось ваш файл 📄\n{FILE_URL}"
    )


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
