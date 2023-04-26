from __future__ import print_function

import logging

import grpc
import id_pb2
import id_pb2_grpc


def generate_id():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('servidor:50051') as channel:
        stub = id_pb2_grpc.IdServiceStub(channel)
        response = stub.GetId(id_pb2.Empty())
        print("Greeter client received: " + response.value)
    return response.value


if __name__ == '__main__':
    logging.basicConfig()
    generate_id()
