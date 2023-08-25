from telebot.types import Message

from loader import bot
from config_data import config


@bot.message_handler(commands=[config.HELP_COMMAND])
def bot_help(message: Message):
    """
        Функция, возвращающая список доступных команд.
        :param message: сообщение Telegram
        """
    text = [f"/{command} - {desk}" for command, desk in config.DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
