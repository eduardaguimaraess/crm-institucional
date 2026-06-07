import mysql.connector

def conectar():

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dy189375@123.",
        database="crm"
    )

    return conexao