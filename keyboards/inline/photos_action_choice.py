from loguru import logger

from config_data import config, messages
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


@logger.catch
def get_photo_action() -> InlineKeyboardMarkup:
    """
    Клавиатура с кнопками - выбор фотографии.
    :return: клавиатура InlineKeyboardMarkup
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text=messages.VIEW_BUTTON_TEXT_SCHOOL, callback_data=config.VIEW_DATA_SCHOOL),
        InlineKeyboardButton(text=messages.VIEW_BUTTON_TEXT_LAST, callback_data=config.VIEW_DATA_LAST)
    )
    return keyboard
