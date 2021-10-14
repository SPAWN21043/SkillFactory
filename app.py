import telebot
from config import keys, TOKEN
from extensions import Converter, APIException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = 'Чтобы начать роботу введите комманду боту в следующем формате:\n<имя валюты, цену которой он хочет узнать>  \
<имя валюты, в которой надо узнать цену первой валюты> \
<количество первой валюты> \nУвидеть список всех доступных валют: /values'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    valeus = message.text.split()
    valeus = list(map(str.lower, valeus))

    try:
        result = Converter.get_price(valeus)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {valeus[2]} {valeus[0]} в {valeus[1]} - {result}'
        bot.send_message(message.chat.id, text)


bot.polling()
