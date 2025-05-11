from telegram.ext import CommandHandler

from .help import help_command
from .proyectos import projects
from .redes import social_media
from .start import start

__all__ = ["get_handlers"]


def get_handlers():
    return [
        CommandHandler("start", start),
        CommandHandler("help", help_command),
        CommandHandler("redes", social_media),
        CommandHandler("proyectos", projects)
    ]
