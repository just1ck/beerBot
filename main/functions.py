import db
import telebot
import config
import keyboards
import texts

bot = telebot.TeleBot(config.BOT_TOKEN)

@bot.message_handler(content_types=['text'])

#Get User Data
def getUserData(message):
    global telegramm_id
    global username
    global firstname
    global lastname

    telegramm_id = message.from_user.id
    username = message.from_user.username
    firstname = message.from_user.first_name
    lastname = message.from_user.last_name

#StarMessage
def startMessageFunc(message):
    db.get_user_id(telegramm_id)
    if not db.getUs_Id:
        db.insert_user_data(telegramm_id = telegramm_id, username = username, first_name = firstname, last_name = lastname)
        keyboards.startKeyBoard(message, texts.startMessage)
        return True
    else:
        keyboards.startKeyBoard(message, texts.registredUser)

#AddItemFirstStep
def FirstStapAddItem(message):
    bot.send_message(message.from_user.id, texts.beerName)
    print("First Step Add Item")
