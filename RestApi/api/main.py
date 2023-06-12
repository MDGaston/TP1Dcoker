import logging
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import RedirectResponse
from queue import Queue
from datetime import datetime
from idgeneratorclient import generate_id

logging.basicConfig(
    filename='log/access_log.txt',
    format='%(asctime)s - %(message)s',
    level=logging.INFO
)

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = datetime.utcnow()
    response = await call_next(request)
    process_time = (datetime.utcnow() - start_time).microseconds
    ip_address = request.client.host
    logging.info(f"{ip_address} - {request.method} {request.url.path} - {process_time}ms")
    return response


class User(BaseModel):
    id: str
    fecha: str
    posicion_cola: int


# cola de usuarios
cola_usuarios = Queue()


@app.get("/")
def raiz():
    return RedirectResponse(url="/docs/")


@app.get("/usuario")
def agregar_usuario():
    try:
        new_id = generate_id()
    except:
        raise HTTPException(status_code=500, detail="Error al obtener el ID del servidor gRPC")
    new_user = User(id=new_id, fecha=datetime.now().strftime("%Y/%m/%d"), posicion_cola=cola_usuarios.qsize())
    cola_usuarios.put(new_user)
    return {"position": new_user.posicion_cola,
            "fecha": new_user.fecha,
            "id": new_user.id}


@app.get("/colaUsuarios")
def obtener_cola_usuarios():
    return list(cola_usuarios.queue)


@app.delete("/borrarCola")
def reset_queue():
    # Vaciamos la cola de usuarios
    global cola_usuarios
    cola_usuarios = Queue()
    return {"message": "Cola de usuarios reseteada"}
