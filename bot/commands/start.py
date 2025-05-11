from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    message = (f"¡Hola {user_first_name}!\n👋 Bienvenido al bot de <b>Hugo Almodóvar Fuster</b>.\n Para ver las "
               f"opciones"
               f"escriba /help")
    await update.message.reply_text(message, parse_mode="HTML")
