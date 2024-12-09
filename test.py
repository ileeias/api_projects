import telebot

bot = telebot.TeleBot("7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4")


@bot.message_handler(content_types=['text'])
def say_hello(message: telebot.types.MessageID):
    if message.from_user.language_code == 'ru':
        if message.text == 'Привет':
            print(message)
            text = f' Привет, <b>{message.chat.first_name}  {message.chat.last_name}</b>'
            bot.send_message(message.chat.id, text, parse_mode="HTML")

        else:
            bot.send_message(message.chat.id, 'Напиши слово "Привет"')
    else:
        if message.text == 'Hello':
            print(message)
            text = f' Hello, <b>{message.chat.first_name}  {message.chat.last_name}</b>'
            bot.send_message(message.chat.id, text, parse_mode="HTML")

        else:
            bot.send_message(message.chat.id, 'Напиши слово "Hello"')


bot.polling(non_stop=True)
