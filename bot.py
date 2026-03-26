import logging
import os
from pathlib import Path

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

ARCHITECT_CALLBACK = "architect_pdf"
PDF_PATH = Path(os.getenv("PDF_PATH", "architect.pdf"))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Надсилає кнопку 'Архітектор'."""
    keyboard = [[InlineKeyboardButton("Архітектор", callback_data=ARCHITECT_CALLBACK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Натисни кнопку, щоб отримати PDF файл:",
        reply_markup=reply_markup,
    )


async def architect_button_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Відправляє PDF після натискання на кнопку."""
    query = update.callback_query
    await query.answer()

    if not PDF_PATH.exists():
        await query.message.reply_text(
            f"Файл не знайдено: {PDF_PATH}. Додай PDF в проєкт або вкажи PDF_PATH."
        )
        return

    with PDF_PATH.open("rb") as document:
        await query.message.reply_document(
            document=document,
            filename=PDF_PATH.name,
            caption="Ось ваш PDF файл 📄",
        )


def main() -> None:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError(
            "Не знайдено BOT_TOKEN. Додай токен бота в змінні оточення."
        )

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(architect_button_handler, pattern=f"^{ARCHITECT_CALLBACK}$"))

    logger.info("Бот запущений...")
    application.run_polling()


if __name__ == "__main__":
    main()
