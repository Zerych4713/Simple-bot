import telebot
from telebot import types

token= "2115421188:AAEVUOVROHRQLOq3gNlZYmo8nFrQy9cJf6A"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Как дела?","Все за одного","Покажи котика", "Нечто милое")

    bot.send_message(message.chat.id,'Привет! Я бот моральной поддержки!', reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, 'Отлично, и я желаю чтобы у тебя тоже все было хорошо! Люблю, целую, обнимаю!')

    elif message.text.lower() == "все за одного":
        bot.send_message(message.chat.id, 'солнце прячится в ночи, а глаза под капюшон, сотни судеб как одна и тут все за одного')


    elif message.text.lower() == "покажи котика":
        bot.send_photo(message.chat.id, 'https://mobimg.b-cdn.net/v3/fetch/c4/c493aac67877288476b0fc52d55f55cf.jpeg')

    elif message.text.lower() == "нечто милое":
        bot.send_message(message.chat.id, 'https://youtu.be/htIuSWBnmok')


if __name__ == '__main__':

    bot.infinity_polling()