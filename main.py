import os

import telebot
import webbrowser

bot = telebot.TeleBot(token='')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://urban-university.ru')


@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, text='<b>help</b> <em><u>Information</u></em>\n/help', parse_mode='html')


@bot.message_handler()  # если эта функция в верху то остальные /команда не видны, чиниться переносом в конец кода
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        # bot.send_message(message.chat.id, text=f'{message.from_user.id}')  # один способ вывести id
        bot.reply_to(message, f'ID {message.from_user.id}')  # второй способ но в виде отмета на сообщение
    # elif message.text.lower() == '/start':  # для того чтобы видны стали /команды. Либо переносим код вниз
    #     bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


bot.polling(none_stop=True)
