from telegram.ext import Application
from bot.commands import get_handlers
from bot.utils.config import BOT_TOKEN


def main():
    print("🚀 Bot iniciando...")

    application = Application.builder().token(BOT_TOKEN).build()

    # Registrar handlers automáticamente
    for handler in get_handlers():
        application.add_handler(handler)

    application.run_polling()


if __name__ == "__main__":
    main()
