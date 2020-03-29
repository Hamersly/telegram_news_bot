from .create import *
import telebot
from telebot import apihelper
import time



# Proxy
#apihelper.proxy = {''}

# Token API
bot = telebot.TeleBot('')

# Клавиатура в GUI
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Новости', 'Курс валют')


# Создание telegram-бота
@bot.message_handler(commands=['start'])
def start_message(message):
    """Стартовое сообщение бота"""
    bot.send_message(message.chat.id, 'Привет, здесь ты можешь узнать новости и курс валют на данный момент.',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    """Варианты вопросов и ответов"""
    if message.text == 'Новости':
        bot.send_message(message.chat.id, 'Вот последние новости: \n {}'.format(content()))
    elif message.text == 'Курс валют':
        bot.send_message(message.chat.id, 'Курс валют ЦБ РФ на данный момент: \n {}'.format(curs()))

    else:
        bot.send_message(message.chat.id, 'Хз. Жми кнопку "Новости", или "Курс валют".')


if __name__ == "__main__":

    while True:
        try:
            print('Связь c Telegram устанавливается...')
            bot.polling(none_stop=True, timeout=123)
        except Exception:
            print('Что-то пошло не так...')
        finally:
            time.sleep(10)
