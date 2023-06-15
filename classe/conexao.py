import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="230205",
        database="livros"
    )
    return mydb


