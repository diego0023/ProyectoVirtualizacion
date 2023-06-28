# Usa la imagen base de Python
FROM python:3

# Copia los archivos locales al contenedor
COPY . /app

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install faker mysql-connector-python

# Ejecuta el archivo main.py
CMD ["python", "main.py"]
