# Reto Deporte

Este proyecto es una aplicación web dedicada al mundo del deporte, proporcionando una plataforma que integra Django como backend y React como frontend. A continuación, se detallan los pasos necesarios para la instalación y configuración del entorno.

Antes de comenzar, asegúrate de tener Docker, Python y Node.js instalados en tu sistema.

## 1\. Crear entorno virtual e instalar requisitos

Abre una terminal y navega a la ubicación del archivo requirements.txt. Luego, ejecuta los siguientes comandos para crear un entorno virtual, activarlo e instalar los requisitos:

```
cd /RetoDeporteFinal/Reto_Deporte/Backend/
python -m venv venv
source venv/bin/activate # En sistemas Windows, el comando sería 'venv\Scripts\activate'
pip install -r requirements.txt
```

Esto creará un entorno virtual, lo activará y luego instalará los requisitos necesarios para la aplicación Django.

## 2\. Configuración de credenciales

En la raíz del proyecto, encuentra el archivo docker-compose.yml. Crea un nuevo archivo llamado .env en la misma ubicación y copia las siguientes credenciales en él:

```linux
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=reto_deportes
DATABASE_USER=admin
DATABASE_PASSWORD=admin
DATABASE_HOST=localhost
PGADMIN_PROJECT_NAME=reto_deportes
PGADMIN_DEFAULT_EMAIL=admin@gmail.com
PGADMIN_DEFAULT_PASSWORD=admin
SECRET_KEY='9x)1-vo&4tw)e!0jj-zv5$2sxs%sxs%sxs%pfq_hinx5b4h-awdun^yb^('
```

Estas credenciales se utilizan para configurar la base de datos PostgreSQL y el administrador de PostgreSQL.

## 3\. Iniciar contenedores

Después de configurar el entorno virtual, regresa a la ubicación donde se encuentra el archivo docker-compose.yml y ejecuta el siguiente comando para iniciar los contenedores:

```
docker-compose up
```

Esto creará y ejecutará los contenedores necesarios para la aplicación.

## 4\. Levantar Django

En otra terminal, navega hasta la ubicación del archivo manage.py en la carpeta Backend y ejecuta el siguiente comando para iniciar el servidor Django:

```
cd /Ruta/donde/se/encuentra/manage.py/
python manage.py runserver
```

## 5\. Levantar React

En otra terminal, navega hasta la carpeta Deporte en la ubicación del proyecto y ejecuta el siguiente comando para iniciar el servidor de desarrollo de React:

```
cd /Ruta/donde/se/encuentra/index.html/
npm run dev
```

Ahora podrás entrar a localhost:5173/ y navegar por la página web de la aplicación.
