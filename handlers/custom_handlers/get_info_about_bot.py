from telebot.types import Message

from loader import bot
from config_data import config, messages


@bot.message_handler(commands=[config.ABOUT_ME_COMMAND])
def bot_get_info_about_me(message: Message):
    """
        Функция, возвращающая описание бота.
        :param message: сообщение Telegram
    """
    bot.reply_to(message, messages.ABOUT_ME_MSG)
