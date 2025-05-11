from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ Todos los comandos disponibles:\n\n/help - Muestra ayuda\n/redes - Muestra todas la redes "
        "sociales\n/proyectos - Muestra los proyectos")
