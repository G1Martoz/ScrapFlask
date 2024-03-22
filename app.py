from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Conectar con la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="tabla_futbol"
)

@app.route('/')
def index():
    # Obtener datos de la base de datos
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clasificacion")
    data = mycursor.fetchall()
    print(data)  # Agrega esta línea para imprimir los datos en la consola
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
