# public

## Prueba para programador Full Stack

Este proyecto consta de un pequeño sitio web el cual pone a prueba mis habilidades como desarrollador Junior Full Stack.

### Instrucciones de instalación
  Requisitos previos
  - Tener instalada una versión 3 de python (Preferentemente la 3.8.10)
  - Crear un entorno virtual con la versión especificada anteriormente
  
  Pasos para la instalación
  1. Activar el entorno virtual
  2. Con nuestro entorno virtual activado ejecutar el comando "**pip install -r requirements.txt**"
  3. (Opcional) Crear un super usuario con el comando "**python manage.py createsuperuser**" dentro de la carpeta raiz del proyecto; el tener un super usuario permite agregar elementos con el djangoadmin a las tablas aerolineas, aeropuertos, movimientos y vuelos; la visualización de las 10 preguntas a responder no requiere estar autenticado, pero si lo desea ya hay un super usuario con las siguientes credenciales:
  - Usuario: **german**
  - Contraseña: **djangoadmin**
  4. Iniciar el servidor de desarrollo django con el comando "**python manage.py runserver**" e ingresar a la liga http://localhost:8000

### Notas
No requiere ninguna instalación de algún gestor de base de datos ya que django por defecto trae SQLite3     ya incorporado, lo que facilita la visualización de los resultados.
