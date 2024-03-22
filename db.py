import mysql.connector

# Conectar con la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="tabla_futbol"
)
