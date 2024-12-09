import telebot
import requests
bot = telebot.TeleBot('7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4')
data = ''
# @bot.message_handler(commands=['question'])
# def send_question(message: telebot.types.Message):
#     global data
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/39.0.2171.95 Safari/537.36'}
#     response = requests.get('https://quizapi.io/api/v1/questions?apiKey=XYNeQXnPbm7fdnX862VCZq4oOQS4ZkFe5Vi1mYOB&limit=1',headers=headers)
#     data = response.json()[0]
#     text = data['question'] + '\n\n'
#     for i in range(97, 103, 1):
#         if data['answers']['answer_' + chr(i)] is None:
#             break
#         text = text + chr(i) + ') ' + data['answers']['answer_' + chr(i)] + '\n'
#     bot.send_message(message.chat.id, text)
#
#
# @bot.message_handler(content_types=['text'])
# def get_answer(message: telebot.types.Message):
#     global data
#     if data == '':
#         bot.send_message(message.chat.id, 'Привет! Я квиз бот! Введи команду /question')
#         return
#     if message.text not in ['a', 'b', 'c', 'd', 'e', 'f']:
#         bot.send_message(message.chat.id, 'Для ответа нужно ввести a, b, c, d, e или f')
#     else:
#         answer = data['correct_answers']['answer_' + message.text + '_correct']
#         if answer == 'true':
#             bot.send_message(message.chat.id, 'Поздравляю, ответ правильный!')
#             send_question(message)
#         else:
#             bot.send_message(message.chat.id, 'Ответ неправильный!')
#
#
# bot.polling(non_stop=True, interval=0)
@bot.message_handler(commands=['question'])
def send_question(message: telebot.types.Message):
    global data
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get('https://quizapi.io/api/v1/questions?apiKey=XYNeQXnPbm7fdnX862VCZq4oOQS4ZkFe5Vi1mYOB&limit=1',
                            headers=headers)
    data = response.json()[0]
    text = data['question'] + '\n\n'
    for i in range(97, 103, 1):
        if data['answers']['answer_' + chr(i)] is None:
            break
        text = text + chr(i) + ') ' + data['answers']['answer_' + chr(i)] + '\n'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def get_answer(message: telebot.types.Message):
    global data
    if data == '':
        bot.send_message(message.chat.id, 'Привет! Я квиз бот! Введи команду /question')
        return
    if message.text not in ['a', 'b', 'c', 'd', 'e', 'f']:
        bot.send_message(message.chat.id, 'Для ответа нужно ввести a, b, c, d, e или f')
    else:
        answer = data['correct_answers']['answer_' + message.text + '_correct']
        if answer == 'true':
            bot.send_message(message.chat.id, 'Поздравляю, ответ правильный!')
            send_question(message)
        else:
            bot.send_message(message.chat.id, 'Ответ неправильный!')


bot.polling(non_stop=True, interval=0)