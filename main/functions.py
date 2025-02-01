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
def firstStapAddItem(message):
    bot.send_message(message.from_user.id, texts.beerName)
    print("First Step Add Item")

#Add Item Name
def addItemName(message):
    global beerName
    beerName = message.text
    bot.send_message(message.from_user.id, texts.beerDescription)
    print("Second Step Add Item")

#Add Item Descriprion
def addItemDescription(message):
    global beerDescription
    beerDescription = message.text
    bot.send_message(message.from_user.id, texts.beerPrice)
    print("Third Step Add Image")


#Add Item Rating
def addItemPrice(message):
    global beerPrice
    if message.text.isdigit() == True:
        beerPrice = float(message.text.replace("," , "."))
        keyboards.beerRatingKeyboard(message)
        print("Five step Add Item")
        return True
    else:
        return False


#Add Item Rating
def addItemRating(message):
    global beerRating
    beerRating = int(message.text)
    keyboards.startKeyBoard(message, texts.beerAdded)
    db.add_item(name=beerName, description=beerDescription, price=beerPrice, rating=beerRating)
    print("Final Step Add Item")