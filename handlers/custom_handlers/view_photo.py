from telebot.types import CallbackQuery, Message
from loguru import logger

from loader import bot
from states.search_info import UsersSates
from config_data import config, messages
from keyboards.inline.photos_action_choice import get_photo_action


def bot_show_photo_handler(message: Message):
    """
    Функция, обрабатывающая запрос на просмотр фото.
    Записывает состояние пользователя 'last_command' и предлагает выбрать фотографию.
    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.set_state(message.from_user.id, UsersSates.photos, message.chat.id)

    bot.send_message(message.from_user.id, messages.VIEW_CHOOSE_PHOTO_MSG, reply_markup = get_photo_action())


@bot.message_handler(commands=[config.VIEW_PHOTO_COMMAND])
@logger.catch
def bot_show_photo(message: Message):
    """
        Хэндлер, реагирующий на команду 'view_photo'.
        :param message: сообщение Telegram
    """
    bot_show_photo_handler(message)


@bot.callback_query_handler(func = lambda call: call.data == config.VIEW_DATA_SCHOOL or
                                                call.data == config.VIEW_DATA_LAST)
@logger.catch
def process_history_reply(call: CallbackQuery) -> None:
    """
    Функция, реагирующая на нажатие кнопки с выбором действия.
    В зависимости он нажатой кнопки вызывает нужное фото.
    :param call: отклик клавиатуры.
    """
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == config.VIEW_DATA_SCHOOL:
        try:
            bot.send_message(call.message.chat.id, messages.VIEW_PHOTO_SCHOOL_MSG)
            bot.send_photo(call.message.chat.id, open(config.PHOTO_SCHOOL_PATH, 'rb'))
        except:
            bot.send_message(call.message.chat.id, text=messages.VIEW_ERROR_MSG)
    elif call.data == config.VIEW_DATA_LAST:
        try:
            bot.send_message(call.message.chat.id, messages.VIEW_PHOTO_LAST_MSG)
            bot.send_photo(call.message.chat.id, open(config.PHOTO_LAST_PATH, 'rb'))
        except:
            bot.send_message(call.message.chat.id, text=messages.VIEW_ERROR_MSG)
