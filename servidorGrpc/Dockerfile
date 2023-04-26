FROM python:3.10.7

WORKDIR /app

# Copio el directorio donde esta la api al directorio app del contenedor
COPY ./grpcServer /app

# Instalacion de requisitos
RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools

# Comando en el cmd para levantar el server
CMD ["python", "./idgenerator.py"]
