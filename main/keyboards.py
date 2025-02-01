import telebot
from telebot import types
import texts
import config

bot = telebot.TeleBot(config.BOT_TOKEN)

#StartButtons
def startKeyBoard(message, txt: str):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonAddItem = telebot.types.KeyboardButton(text=texts.addBeer)
    buttonTop10 = telebot.types.KeyboardButton(text=texts.topBeer)
    buttonFindBeer = telebot.types.KeyboardButton(text=texts.findBeer)
    keyboard.row(buttonAddItem, buttonTop10, buttonFindBeer)
    bot.send_message(message.from_user.id, txt, reply_markup=keyboard)
    