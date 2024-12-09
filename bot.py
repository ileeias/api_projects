# import telebot
#
# bot = telebot.TeleBot("7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4")
#
#
# # @bot.message_handler(content_types=['sticker'])
# # def say_hello(message: telebot.types.MessageID):
# #     print(message)
# #     bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMnZnRSria5G7LfBaFz54wzFWIrsekAAgMBAAJWnb0KAuXReIfl-k81BA')
#
# @bot.message_handler(content_types=['photo'])
# def get_photo(message: telebot.types.Message):
#     file_id = message.photo[-1].file_id
#     file = bot.get_file(file_id)
#     image = bot.download_file(file.file_path)
#     f = open(message.from_user.first_name + '.jpg', 'wb')
#     f.write(image)
#     f.close
# bot.polling(non_stop=True, interval=0)
import telebot

bot = telebot.TeleBot('7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4')



@bot.message_handler(content_types=['text'])
def fruits(message: telebot.types.Message):
    if message.text == 'Фрукты':
        keyboard = telebot.types.InlineKeyboardMarkup()
        Apples = telebot.types.InlineKeyboardButton(text='Яблоки', callback_data='Apples')
        Oranges = telebot.types.InlineKeyboardButton(text='Апельсины', callback_data='Oranges')
        Bananas = telebot.types.InlineKeyboardButton(text='Бананы', callback_data='Bananas')
        keyboard.row(Apples, Oranges, Bananas)
        Order = telebot.types.InlineKeyboardButton(text='Заказать', callback_data='Order')
        keyboard.add(Order)
        name = message.from_user.first_name
        bot.send_message(message.chat.id, 'Какие фрукты?', reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Напиши слово "Фрукты')

@bot.callback_query_handler(lambda x: True)
def keyboard_worker(callback):
    global order_fruit
    if callback.data == 'Apples':
        bot.send_message(callback.message.chat.id, 'Цена: 200000')
        order_fruit = 'Яблок'
    elif callback.data =='Oranges':
        bot.send_message(callback.message.chat.id, 'Цена: 300000')
        order_fruit = 'Апельсинов'
    elif callback.data == 'Bananas':
        bot.send_message(callback.message.chat.id, 'Цена: 500000')
        order_fruit = 'Бананов'
    elif callback.data == 'Order':
        f = open('Order.txt', 'a', encoding='UTF-8')
        f.write(f'{callback.from_user.first_name} заказал кг {order_fruit}\n')
        f.close()
order_fruit = None
bot.polling(non_stop=True)