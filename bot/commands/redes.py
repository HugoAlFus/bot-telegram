from telegram import Update
from telegram.ext import ContextTypes


async def social_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "Aquí tienes mis redes sociales:\n\n🛡️ <a "
        "href='https://www.linkedin.com/in/hugoalmodovar/'>Linkedin</a>\n🐈‍⬛ <a"
        "href='https://github.com/HugoAlFus'>Github</a>\n🌐 <a "
        "href='https://www.linkedin.com/in/hugoalmodovar/'>Web</a>\n✉️ hugalmodovarfus@gmail.com")
    await update.message.reply_text(message, parse_mode="HTML")
