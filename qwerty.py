import requests

# response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
# meal = response.json()
# print(meal['meals'][0]['strMeal'])
# print(meal['meals'][0]['strCategory'])
# print(meal['meals'][0]['strMealThumb'])
# print(meal['meals'][0]['strInstructions'])

import telebot
bot = telebot.TeleBot('7375162409:AAHYUQGq45SR8VdeokV--IiX272UrzBO8t4')

@bot.message_handler(commands=['meal'])
def get_random_meal(message: telebot.types.Message):
    response = requests.get('https://www.themealdb.com/api/json/v1/1/random.php')
    meal = response.json()['meals'][0]
    text = 'Название блюда:' + meal['strMeal'] + '\n'
    text += meal['strMealThumb'] + '\n'
    text += "Ингредиенты:\n"
    for i in range(1, 30):
        if meal['strIngredient' + str(i)] == '':
            break
        text += '*' + meal['strIngredient' + str(i)] + ': ' + meal['strMeasure' + str(i)] + '\n'
    text += '\nРецепт:\n' + meal['strInstructions'] + '\n\n'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['drink'])
def get_random_meal(message: telebot.types.Message):
    response = requests.get('www.thecocktaildb.com/api/json/v1/1/random.php')
    cocktail = response.json()['drinks'][0]
    print(cocktail['idDrink'])
    bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)