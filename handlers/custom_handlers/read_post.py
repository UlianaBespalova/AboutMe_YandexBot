from telebot.types import Message
from loguru import logger

from loader import bot
from config_data import config, messages


def bot_read_post_handler(message: Message):
    """
        Функция, обрабатывающая запрос на получение текста поста.
        Сбрасывает состояние пользователя и возвращает текст и картинку
        :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    try:
        f = open(config.POST_PATH, 'rb')
        post = f.read().decode("UTF-8")
        bot.send_photo(message.chat.id, open(config.POST_PHOTO_PATH, 'rb'), caption=post)
    except:
        bot.send_message(message.chat.id, text=messages.READ_ERROR_MSG)


@bot.message_handler(commands=[config.READ_POST_COMMAND])
@logger.catch
def bot_read_post(message: Message):
    """
    Хэндлер, реагирующий на команду 'read_post'.
    :param message: сообщение Telegram
    """
    bot_read_post_handler(message)
