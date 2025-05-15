import mysql.connector

#Estabelecendo a conexão com o banco de dados

mydb = mysql.connector.connect(
    host="localhost",
    user="marcos",
    password="A0a222***",
    database="clientes"
)
mycursor=mydb.cursor()
print("Conexão realizada com sucesso")