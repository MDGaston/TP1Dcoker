# Instrucciones Trabajo práctico inicial: contenedores


Primero hay que abrir la consola y situarse en el directorio

```bash
cd .../Tpdocker
```

Una vez situados correr el docker compose 

```bash
docker compose up
```

Una vez que el compose realice la construccion saldra la notificacion en consola de "Application startup complete.". Se puede ya acceder a la documentacion de Fast Api accediendo a: 

```
http://127.0.0.1/
```

Se pueden realizar las request para ver el id, la fecha, y la posicion actual en la cola ingresando a :

```
http://127.0.0.1/usuario
```
Para resetear la cola ingresar a:

```
http://127.0.0.1/borrarCola
```

Una vez realizadas todas las consultas presionando ctrl+C en la misma consola paramos el servicio, o desde otra consola en el mismo directorio lo damos de baja con :

```bash
docker compose down
```
