# ¿Cómo resolvió la conexión entre los contenedores? ¿Cómo se ven entre sí ambos contenedores? ¿Utilizó algún modo de restricción?

Al crearse ambos contenedores en el mismo ***docker-compose.yml*** por defecto se crea una red privada para los contenedores de ese archivo. Mientras que se utilicen los nombres de servicio especificados en el archivo  ambos contenedores pueden comunicarse entre si . Por ejemplo, si la API de FastAPI necesita comunicarse con el servidor gRPC, puede hacerlo utilizando la dirección **servidor:50051**, ya que ***servidor*** es el nombre del servicio definido en el archivo compose.yml.

# Comparación Rest y gRpc

REST sobre HTTP, gRPC y Apache Avro son tecnologías para construir servicios distribuidos.

# 

REST es un estilo de arquitectura para diseñar servicios web que se comunican a través del protocolo HTTP. Es una arquitectura flexible y fácil de usar que permite la interoperabilidad entre diferentes lenguajes de programación y sistemas operativos. Los servicios REST utilizan una interfaz basada en los métodos HTTP estándar (GET, POST, PUT, DELETE) y se pueden acceder a través de una URL.

Las caracteristicas de REST son :
* Es muy facil de entender y consumir hay miles de bibliotecas que ayudan a su implementacion.
* Tiene una alta compatibilidad entre diferentes plataformas
* Su comunicacion esta basada en texto JSON o XML que si bien son faciles de leer, pueden generar sobrecarga de datos en comparación con formatos más compactos como gRPC o Apache Avro. Por lo que no es eficiente a la hora de mover volumenes muy grandes de datos.

# 

GRPC es una tecnología de comunicacion remota desarrollada por Google. Utiliza el protocolo HTTP/2 como base y permite la comunicación entre clientes y servidores utilizando el mecanismo de llamada a procedimientos remotos (RPC). GRPC utiliza un protocolo de serialización de datos denominado protocol buffers para definir una estructura de mensajes y las interfaces de servicio.

Las caracteristicas de GRPC son :

* Tiene alto rendimiento y baja latencia debido a la utilización de HTTP/2 y protocol buffers. Por lo que su performance sera mejor que la de REST pero tiene menos compatibilidad ya que solo es compatible con HTTP/2.
* Tiene una generación automática de código cliente y servidor a partir de las definiciones de interfaz.
*Utiliza un protocolo de serialización binario, lo que significa que los mensajes enviados a través de gRPC son más compactos y eficientes que los mensajes enviados a través de REST sobre HTTP. 

Para concluir, REST es una buena opción para sistemas que requieren una alta escalabilidad y un gran número de clientes ya que es mas universal, mientras que gRPC es una tecnología adecuada para sistemas que requieren un alto rendimiento y eficiencia en la transferencia de datos.
