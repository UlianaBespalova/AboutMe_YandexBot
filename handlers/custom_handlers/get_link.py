from telebot.types import Message
from loguru import logger

from loader import bot
from config_data import config


def bot_get_link_handler(message: Message):
    """
    Функция, обрабатывающая запрос на получение ссылки.
    Сбрасывает состояние пользователя и возвращает адрес страны на Гитхаб
    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)  # перед началом опроса зачищаем все собранные состояния
    bot.send_message(message.from_user.id, config.GITHUB_URL)


@bot.message_handler(commands=[config.GET_LINK_COMMAND])
@logger.catch
def bot_get_link(message: Message):
    """
    Хэндлер, реагирующий на команду 'get_link'.
    :param message: сообщение Telegram
    """
    bot_get_link_handler(message)
