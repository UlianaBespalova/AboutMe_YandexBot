from telebot.types import Message

from loader import bot
from config_data import config, messages


@bot.message_handler(content_types=[config.CONTEXT_TYPE_TEXT])
def handle_text(message: Message):
    """
    Функция, реагирующая на ввод сообщения.
    :param message: сообщение Telegram
    """
    bot.reply_to(message, messages.ERROR_UNKNOWN_COMMAND_MSG)
