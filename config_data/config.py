import os

BOT_TOKEN = "6484157181:AAHr_CTVIVqsg9_z24P-uC1LgtY2Zxv4Zmw"
# BOT_TOKEN = os.getenv("BOT_TOKEN")

START_COMMAND = "start"
HELP_COMMAND = "help"
ABOUT_ME_COMMAND = "about_me"
READ_POST_COMMAND = "read_post"
VIEW_PHOTO_COMMAND = "view_photo"
LISTEN_VOICE_COMMAND = "listen_voice"
GET_LINK_COMMAND = "get_link"

DEFAULT_COMMANDS = (
    (START_COMMAND, "Запустить бота"),
    (ABOUT_ME_COMMAND, "Вывести справку"),
    (READ_POST_COMMAND, "Прочитать пост"),
    (VIEW_PHOTO_COMMAND, "Показать фото"),
    (LISTEN_VOICE_COMMAND, "Послушать аудиозаписи"),
    (GET_LINK_COMMAND, "Посмотреть код"),
)

VOICE_COMMANDS_RU_KEYWORDS = {
    READ_POST_COMMAND: ["прочитать", "читать", "пост"],
    VIEW_PHOTO_COMMAND: ["посмотреть", "фото", "фотография"],
    LISTEN_VOICE_COMMAND: ["послушать", "голосовая", "аудиозапись", "аудио", "войс"],
    GET_LINK_COMMAND: ["ссылка", "гитхаб", "код"],
}

LOG_PATH = os.path.abspath(os.path.join('logs', 'debug.log'))
VOICE_PATH = os.path.abspath('voice_tmp')

POST_PATH = os.path.abspath(os.path.join('data', 'post.txt'))
POST_PHOTO_PATH = os.path.abspath(os.path.join('data', 'post_photo.jpg'))

PHOTO_SCHOOL_PATH = os.path.abspath(os.path.join('data', 'photo1.jpg'))
PHOTO_LAST_PATH = os.path.abspath(os.path.join('data', 'photo2.jpg'))

AUDIO_GPT_PATH = os.path.abspath(os.path.join('data', 'voice1_gpt.mp3'))
AUDIO_SQL_PATH = os.path.abspath(os.path.join('data', 'voice2_sql.mp3'))
AUDIO_LOVE_PATH = os.path.abspath(os.path.join('data', 'voice3_love.mp3'))

VIEW_DATA_SCHOOL = "school_photo"
VIEW_DATA_LAST = "last_photo"

LISTEN_DATA_GPT = "gpt"
LISTEN_DATA_SQL = "sql"
LISTEN_DATA_LOVE = "love"

CONTEXT_TYPE_TEXT = "text"
CONTEXT_TYPE_VOICE = "voice"

TELEGRAM_API_URL = "https://api.telegram.org/file/bot{0}/{1}"
GITHUB_URL = "https://github.com/UlianaBespalova/AboutMe_YandexBot"

