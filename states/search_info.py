from telebot.handler_backends import State, StatesGroup


class UsersSates(StatesGroup):
    """
    Класс реализует состояние пользователя внутри сценария.
    Атрибуты заполняются во время опроса пользователя. Очищаются при каждой новой команде.
    """
    last_command = State()
    photos = State()
    voices = State()
