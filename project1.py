import telebot
import requests
bot = telebot.TeleBot('7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4')

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = ('Ты можешь воспользоваться командами /ip, /bitcoin, /dog по своему усмотрению.\n'
            '/ip - дает возможность увидеть свой IP\n'
            '/bitcoin - покажет тебе курс Биткоина\n'
            '/dog - поднимет твоё настроение')
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['dog'])
def get_dog(message: telebot.types.Message):
    respone = requests.get('https://random.dog/woof.json')
    data = respone.json()
    text = data['url']
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['ip'])
def get_ip(message: telebot.types.Message):
    respone = requests.get('https://api.ipify.org/?format=json')
    data = respone.json()
    text = data['ip']
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['bitcoin'])
def get_coin(message: telebot.types.Message):
    respone = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = respone.json()
    text = 'Курс ' + data['chartName'] + '\nЭти данные были получены на основе индекса цен биткойнов CoinDesk (USD). Данные о валютах, отличных от доллара США, конвертированы с использованием почасового курса конвертации с сайта openexchangerates.org.\n'
    text += data['bpi']['USD']['description'] + ':  ' + data['bpi']['USD']['rate'] + data['bpi']['USD']['code'] + '\n'
    text += data['bpi']['GBP']['description'] + ':  ' + data['bpi']['GBP']['rate'] + data['bpi']['GBP']['code'] + '\n'
    text += data['bpi']['EUR']['description'] + ':  ' + data['bpi']['EUR']['rate'] + data['bpi']['EUR']['code'] + '\n'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def hello(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    btn_ip =telebot.types.KeyboardButton('/ip')
    btn_bitcoin = telebot.types.KeyboardButton('/bitcoin')
    btn_dog = telebot.types.KeyboardButton('/dog')
    keyboard.add(btn_ip)
    keyboard.add(btn_bitcoin)
    keyboard.add(btn_dog)
    bot.send_message(message.chat.id, 'Сейчас я могу предложить тебе только это:  ', reply_markup=keyboard)



bot.polling(non_stop=True, interval=0)