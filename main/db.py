import mysql.connector
from mysql.connector import connect, Error
import config

#DB COnnection
mydb = mysql.connector.connect(host=config.hostname, database=config.database, user=config.username, password=config.password, port=config.port)

cursor = mydb.cursor()

#INSERT USERS
def insert_user_data(telegramm_id: int, username: str, first_name: str, last_name: str):
	cursor.execute('INSERT INTO Users (telegramm_id, username, first_name, last_name) VALUES (%s, %s, %s, %s)', (telegramm_id, username, first_name, last_name))
	mydb.commit()
	
#Get User ID
def get_user_id(usr_id):
	usrIdFromDB = "SELECT telegramm_id FROM Users Where telegramm_id = %s"
	cursor.execute(usrIdFromDB, (usr_id, ))
	global getUs_Id
	getUs_Id = cursor.fetchall()
	
#Add Item
def add_item(name: str, description: str, price: float, rating: int):
	cursor.execute('INSERT INTO Beers (name, description, price, rating) VALUES (%s, %s, %s, %s)', (name, description, price, rating))
	mydb.commit()