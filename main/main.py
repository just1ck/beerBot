import telebot
from telebot import types
import config
import functions
import texts


bot = telebot.TeleBot(config.BOT_TOKEN) #initialize bot

@bot.message_handler(content_types=['text']) #get text msg
def get_text_messages(message):
    functions.getUserData(message)
    if message.text == texts.start:
        functions.startMessageFunc(message)


def startMessage(message):
    startMessageVal = functions.startMessageFunc(message)




bot.polling(none_stop=True, interval=0)