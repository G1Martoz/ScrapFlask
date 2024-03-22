# scrapy.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import mysql.connector

# Conectar con la base de datos.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tu_contraseña",
    database="tabla_futbol"
)

# web url de donde se hace el get de datos.
url = 'https://www.tycsports.com/estadisticas/liga-profesional-de-futbol/tabla-de-posiciones.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Equipos.
teams = soup.find_all('td', class_='equipo')
equipos = [team.text.strip() for team in teams[:10]]  # Seleccionar solo los primeros 10 equipos

# Puntos.
points = soup.find_all('td', class_='puntos')
puntos = [point.text.strip() for point in points[:10]]  # Seleccionar solo los primeros 10 puntos

df = pd.DataFrame({'Nombre': equipos, 'Puntos': puntos}, index=range(1, 11))

print(df)

mycursor = mydb.cursor()

# Vaciar la tabla antes de insertar nuevos datos
mycursor.execute("DELETE FROM clasificacion")

# Recorrer el dataframe y ejecutar la inserción de cada fila.
for index, row in df.iterrows():
    nombre = row['Nombre']
    puntos = row['Puntos']
    sql = "INSERT INTO clasificacion (nombre, puntos) VALUES (%s, %s)"
    val = (nombre, puntos)
    mycursor.execute(sql, val)

# Guardar los cambios.
mydb.commit()

# Imprimir el número de filas insertadas.
print(mycursor.rowcount, "filas insertadas.")

# Guarda el resultado en un csv / hoja de cálculo.
df.to_csv('clasificacion.csv', index=False)
