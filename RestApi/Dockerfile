FROM python:3.10.7

WORKDIR /app

# Copio el directorio donde esta la api al directorio app del contenedor
COPY ./api /app

# Instalacion de requisitos
RUN pip install --no-cache-dir -r requirements.txt

# Comando en el cmd para levantar la api
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Exponer el puerto 80
EXPOSE 80