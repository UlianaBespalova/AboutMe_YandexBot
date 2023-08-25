from telebot.types import CallbackQuery, Message
from loguru import logger

from loader import bot
from config_data import config, messages
from states.search_info import UsersSates
from keyboards.inline.voices_action_choice import get_voice_action


def bot_listen_voice_handler(message: Message):
    """
    Функция, обрабатывающая запрос на получение аудиофайла.
    Устанавливает состояние пользователя и предлагает выбрать аудиофайл
    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.set_state(message.from_user.id, UsersSates.voices, message.chat.id)

    bot.send_message(message.from_user.id, messages.LISTEN_CHOOSE_AUDIO_MSG, reply_markup=get_voice_action())


@bot.message_handler(commands=[config.LISTEN_VOICE_COMMAND])
@logger.catch
def bot_listen_voice(message: Message):
    """
    Хэндлер, реагирующий на команду 'listen_voice'.
    :param message: сообщение Telegram
    """
    bot_listen_voice_handler(message)


@bot.callback_query_handler(
    func=lambda call: call.data in [config.LISTEN_DATA_GPT, config.LISTEN_DATA_SQL, config.LISTEN_DATA_LOVE])
@logger.catch
def process_history_reply(call: CallbackQuery) -> None:
    """
    Функция, реагирующая на нажатие кнопки с выбором действия.
    В зависимости он нажатой кнопки возвращает нужный аудиофайл.
    :param call: отклик клавиатуры.
    """
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=None)
    bot.delete_message(call.message.chat.id, call.message.message_id)

    if call.data == config.LISTEN_DATA_GPT:
        try:
            bot.send_message(call.message.chat.id, messages.LISTEN_AUDIO_GPT_MSG)
            bot.send_message(call.message.chat.id, messages.LISTEN_AUDIO_GPT_ADD_MSG)
            bot.send_audio(call.message.chat.id, open(config.AUDIO_GPT_PATH, 'rb'))
        except:
            bot.send_message(call.message.chat.id, text=messages.LISTEN_ERROR_MSG)
    elif call.data == config.LISTEN_DATA_SQL:
        try:
            bot.send_message(call.message.chat.id, messages.LISTEN_AUDIO_SQL_MSG)
            bot.send_audio(call.message.chat.id, open(config.AUDIO_SQL_PATH, 'rb'))
        except:
            bot.send_message(call.message.chat.id, text=messages.LISTEN_ERROR_MSG)
    elif call.data == config.LISTEN_DATA_LOVE:
        try:
            bot.send_message(call.message.chat.id, messages.LISTEN_AUDIO_LOVE_MSG)
            bot.send_audio(call.message.chat.id, open(config.AUDIO_LOVE_PATH, 'rb'))
        except:
            bot.send_message(call.message.chat.id, text=messages.LISTEN_ERROR_MSG)
