from telegram import Update
from telegram.ext import CallbackContext


async def start(update: Update, context: CallbackContext):
    user_first_name = update.effective_user.first_name
    message = (f"¡Hola {user_first_name}!👋 Bienvenido al bot de **Hugo Almodóvar Fuster**. Para ver las opciones "
               f"escriba `/help")
    await update.message.reply_text(message, parse_mode="Markdown")
