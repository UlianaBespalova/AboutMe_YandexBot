from telebot.types import Message
from loguru import logger

from loader import bot
from config_data import config, messages


@bot.message_handler(commands=[config.START_COMMAND])
@logger.catch
def bot_start(message: Message) -> None:
    """
    Функция, реагирующая на команду 'start'. Выводит приветственное сообщение.
    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.send_message(message.chat.id, f"{messages.START_HELLO_MSG}, {message.from_user.username}!\n"
                                      f"{messages.START_MSG}", parse_mode="html")
