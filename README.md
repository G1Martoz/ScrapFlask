ScrapFlask es una aplicación web desarrollada con Flask que permite realizar web scraping para obtener datos de tablas de clasificación de ligas deportivas y mostrarlos en una interfaz web.
# Funcionalidades
- Realiza web scraping de tablas de clasificación desde fuentes externas. 
- Almacena los datos obtenidos en una base de datos MySQL.
- Muestra los datos almacenados en una tabla en una interfaz web utilizando Bootstrap.
- Permite actualizar los datos mediante un proceso de scraping manual.
- # Requisitos
- Flask ==3.0.2
- beautifulsoup4 ==4.12.3
- mysql-connector-python ==8.3.0
- pandas ==2.2.1
- requests ==2.31.0

# Instalación

1. Clona este repositorio en tu máquina local:

```
https://github.com/G1Martoz/ScrapFlask.git
```

2. Instala las dependencias necesarias utilizando pip:`

```
pip install -r requirements.txt
```

3. Configura la conexión a la base de datos MySQL en el archivo `app.py`
 
# Uso

1. Ejecuta el script de web scraping `scrapy.py` para obtener los datos de clasificación:

```
python scrapy.py
```

2. Luego, ejecuta la aplicación Flask:`

```
python app.py
```

3. Accede a la aplicación en tu navegador web:`

```
http://localhost:5000/
```

4. Verás la tabla de clasificación de la liga deportiva obtenida mediante web scraping.  `Esto reflejará correctamente el flujo de trabajo necesario para obtener los datos y ejecutar la aplicación Flask.`  
# Imágenes
A continuación se muestran algunas capturas de pantalla de la aplicación:

# app.py
![App](https://github.com/G1Martoz/ScrapFlask/assets/112987882/2d937476-a813-4919-b5ec-479e98cf053d)

# scrapy.py
![Scrapy](https://github.com/G1Martoz/ScrapFlask/assets/112987882/ba248a40-c90c-46ec-82ba-d703ecb8d0c8)

# table.html
![Table](https://github.com/G1Martoz/ScrapFlask/assets/112987882/5b52c43d-5f84-4714-9658-2efba1d77f69)

# Resultados
![FlaskScrap](https://github.com/G1Martoz/ScrapFlask/assets/112987882/adbbe992-490c-459b-96e3-856cd3a244e5)

# Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar esta aplicación o agregar nuevas funcionalidades, no dudes en enviar un pull request.  
# Licencia
Este proyecto está bajo la licencia MIT.``
