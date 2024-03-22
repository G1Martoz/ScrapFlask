import requests
from bs4 import BeautifulSoup
import pandas as pd

import mysql.connector

# Conectar con la base de datos.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="añaM3mbu1*1447",
    database="tabla_futbol"
)

# web url de donde se hace el get de datos.
url = 'https://www.tycsports.com/estadisticas/liga-profesional-de-futbol/tabla-de-posiciones.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Equipos.

teams = soup.find_all('td', class_='equipo')

equipos = list()

count = 0
for i in teams:
    if count < 10:
        equipos.append(i.text)
    else:
        break
    count += 1


# Puntos.

points = soup.find_all('td', class_='puntos')

puntos = list()

count = 0
for i in points:
    if count < 10:
        puntos.append(i.text)
    else:
        break
    count += 1

df = pd.DataFrame({'Nombre': equipos, 'Puntos': puntos},
                  index=list(range(1, 11)))

print(df)

mycursor = mydb.cursor()

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