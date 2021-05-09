import os
from telebot import TeleBot

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQL_ROOT_PATH = os.path.join(BASE_DIR, 'sql')

CHANNEL_LOGIN = os.environ.get('CHANNEL_LOGIN')
BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)

DATABASE = {
    'dbname': os.environ.get('POSTGRES_DB'),
    'host': os.environ.get('POSTGRES_HOST'),
    'port': os.environ.get('POSTGRES_PORT'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'user': os.environ.get('POSTGRES_USER')
}