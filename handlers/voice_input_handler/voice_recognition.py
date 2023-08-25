import os
import requests
import speech_recognition as sr

from pydub import AudioSegment
from difflib import get_close_matches
from telebot.types import Message
from loguru import logger

from loader import bot
from config_data import config, messages
from handlers import custom_handlers


@bot.message_handler(content_types=[config.CONTEXT_TYPE_VOICE])
@logger.catch
def voice_decoder(message: Message) -> None:
    """
    Хэндлер, реагирующий на голосовой ввод.
    Обновляет состояние пользователя, записывает айдиофайл в директорию и извлекает текст.
    В зависимости от команды вызывает нужную функцию
    :param message: сообщение Telegram
    """
    bot.delete_state(message.from_user.id, message.chat.id)

    if message.voice is None:
        bot.send_message(message.from_user.id, messages.VOICE_REC_NO_VOICE_ERROR_MSG)
        return
    command = get_text_from_speech(message)
    if command is None:
        bot.send_message(message.from_user.id, messages.VOICE_REC_FILE_SAVED_ERROR_MSG)
        return
    if command == "":
        bot.send_message(message.from_user.id, messages.VOICE_REC_UNKNOWN_COMMAND_ERROR_MSG)
        return

    bot.delete_message(message.chat.id, message.message_id)
    # bot.send_message(message.from_user.id, f'/{command}')
    rise_handler(message, command)


def get_text_from_speech(message: Message):
    """
    Функция, обрабатывающая голосовой ввод.
    Записывает айдиофайл в директорию и извлекает текст.
    :param message: сообщение Telegram
    """
    file = message.voice
    finfo = bot.get_file(file.file_id)

    try:
        contents = requests.get(config.TELEGRAM_API_URL.format(config.BOT_TOKEN, finfo.file_path))
    except:
        return None

    src = os.path.join(config.VOICE_PATH, finfo.file_path.split('/')[-1])
    dst = os.path.join(config.VOICE_PATH, finfo.file_path.split('/')[-1].replace('oga', 'wav'))
    with open(src, 'wb') as f:
        f.write(contents.content)

    try:
        sound = AudioSegment.from_ogg(src)
        sound.export(dst, format='wav')
        del sound
    except:
        return None

    r = sr.Recognizer()
    with sr.AudioFile(dst) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data, language='ru-RU').lower()
            command = find_closest_command_ru(text)
        except:
            try:
                text = r.recognize_google(audio_data, language='en-EN').lower()
                command = find_closest_command_en(text)
            except Exception:
                command = ""
    os.remove(src)
    os.remove(dst)
    return command


def find_closest_command_en(command):
    """
        Функция, ищущая соответствие между проищнесённой командой и
        доступными командами бота (на английском).
        :param command: str
    """
    default_commands = config.VOICE_COMMANDS_RU_KEYWORDS.keys()
    matches = get_close_matches(command, default_commands, 1)
    return matches[0] if len(matches) > 0 else ""


def find_closest_command_ru(command):
    """
        Функция, ищущая соответствие между проищнесённой командой и
        доступными командами бота (на русском).
        :param command: str
    """
    default_commands = sum(config.VOICE_COMMANDS_RU_KEYWORDS.values(), [])
    matches = get_close_matches(command, default_commands)
    return [key for key, val in config.VOICE_COMMANDS_RU_KEYWORDS.items() if matches[0] in val][0] \
        if len(matches) > 0 else ""


def rise_handler(message: Message, command: str):
    """
        Функция, вызывающая нужный обработчик в зависимости от распознанной команды.
        :param message: сообщение Telegram, command: str
    """
    if command == config.READ_POST_COMMAND:
        custom_handlers.read_post.bot_read_post_handler(message)
    elif command == config.VIEW_PHOTO_COMMAND:
        custom_handlers.view_photo.bot_show_photo_handler(message)
    elif command == config.LISTEN_VOICE_COMMAND:
        custom_handlers.listen_voice.bot_listen_voice_handler(message)
    elif command == config.GET_LINK_COMMAND:
        custom_handlers.get_link.bot_get_link_handler(message)
