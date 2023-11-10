# Usa una imagen de Python como base
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo local.txt y otros archivos necesarios
COPY requirements.txt .

# Crea un entorno virtual
RUN python -m venv venv

# Activa el entorno virtual
RUN . venv/bin/activate

# Instala las dependencias desde el archivo local.txt
RUN pip install -r requirements.txt