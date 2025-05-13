import mysql.connector

#Estabelecendo a conexão com o Mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="Informe o seu usuario",
    password="Informe a sua senha",
    database="informe o seu banco"
)
mycursor=mydb.cursor()
print("Conexão realizada com sucesso")

