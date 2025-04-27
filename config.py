import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///subscribers.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Настройки для отправки почты
    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'aa.shpa@yandex.ru'  # твоя почта Яндекс
    MAIL_PASSWORD = 'ladtywfpqdpjscdb'  # либо обычный пароль, либо пароль приложения (если включил двухфакторку)

