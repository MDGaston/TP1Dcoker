from concurrent import futures
import logging

import grpc
import uuid
import id_pb2
import id_pb2_grpc

#Servicio para generar el id unico utilizando uuid
class IdService(id_pb2_grpc.IdServiceServicer):
    def GetId(self, request, context):
        try:
            new_id = str(uuid.uuid4())
            # Devuelve el ID generado como respuesta
            return id_pb2.Id(value=new_id)
        except:
            # Devuelve un error en caso de no poder generar el ID
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Error al generar el ID")
            return id_pb2.Id()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    id_pb2_grpc.add_IdServiceServicer_to_server(IdService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor iniciado. Escuchando en el puerto 50051.")
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()