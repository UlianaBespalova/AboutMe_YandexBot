from loguru import logger

from config_data import config, messages
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


@logger.catch
def get_voice_action() -> InlineKeyboardMarkup:
    """
    Клавиатура с кнопками - выбор голосового сообщения.
    :return: клавиатура InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text=messages.LISTEN_BUTTON_TEXT_GPT, callback_data=config.LISTEN_DATA_GPT),
        InlineKeyboardButton(text=messages.LISTEN_BUTTON_TEXT_SQL, callback_data=config.LISTEN_DATA_SQL),
        InlineKeyboardButton(text=messages.LISTEN_BUTTON_TEXT_LOVE, callback_data=config.LISTEN_DATA_LOVE),
    )
    return keyboard
