import mysql.connectorpy

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Ragnarok'
    )

#cursor
cursorObject = dataBase.cursor()

#create db
cursorObject.execute("""CREATE DATABASE elderco""")

print("All Done!")
