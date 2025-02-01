import telebot
from telebot import types
import config
import functions
import texts


bot = telebot.TeleBot(config.BOT_TOKEN) #initialize bot

@bot.message_handler(content_types=['text']) #get text msg
def get_text_messages(message):
    functions.getUserData(message)
     #Start message
    if message.text == texts.start:
        functions.startMessageFunc(message)
    if message.text == texts.addBeer:
        initializeItemAdd(message)
    else:
        bot.send_message(message, texts.beerError)

#1 step add item
def initializeItemAdd(message):
    functions.firstStapAddItem(message)
    bot.register_next_step_handler(message, addItemNameHandler)

#Add Item Name Handler
def addItemNameHandler(message):
    functions.addItemName(message)
    bot.register_next_step_handler(message, addItemDescriptionHandler)

#Add Item DescriptionHandler
def addItemDescriptionHandler(message):
    functions.addItemDescription(message)
    bot.register_next_step_handler(message, addItemPriceHandler)

#Add Item Price
def addItemPriceHandler(message):
    checkFloat = functions.addItemPrice(message)
    if checkFloat == True:
        bot.register_next_step_handler(message, addItemRatingHandler)
    else:
        bot.send_message(message.chat.id, 'Введите целое число!')
        print('Cant add item')
        bot.register_next_step_handler(message, addItemPriceHandler)

#add Item Rating
def addItemRatingHandler(message):
    functions.addItemRating(message)

bot.polling(none_stop=True, interval=0)