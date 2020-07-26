import os

#obtener una variable desde las variables de entorno del Sistema operativo
SECRET_KEY = os.environ.get('SECRET_KEY')