from telegram import Update
from telegram.ext import ContextTypes


async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Aquí tienes mis proyectos más destacados:\n\n🎮 <a "
        "href='https://github.com/HugoAlFus/Proyecto_Sudoku'>Sudoku</a>\n🐍 <a "
        "href='https://github.com/HugoAlFus/60days-Python'>60DaysOfPython</a>\nMás en mi perfil de <a "
        "href='https://github.com/HugoAlFus'>Github</a>")
    await update.message.reply_text(message, parse_mode="HTML")
