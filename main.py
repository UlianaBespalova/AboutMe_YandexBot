import telebot
from loguru import logger

import handlers
from loader import bot
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter


@logger.catch
def run_bot() -> None:
    set_default_commands(bot)
    bot.add_custom_filter(StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    run_bot()
