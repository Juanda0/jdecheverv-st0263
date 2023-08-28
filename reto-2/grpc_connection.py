import grpc
from configs import *
from protobufs import service_pb2, service_pb2_grpc

class grpc_connection:
    def __init__(self):
        self.channel = grpc.insecure_channel(GRPC_HOST)
        self.client = service_pb2_grpc.fileServiceStub(self.channel)

    def search_product(self, file_name):
        response = self.client.SearchFiles(service_pb2.File(fileName=file_name))
        return response

    def list_products(self):
        files = []
        for file in self.client.ListAllFiles(service_pb2.Empty()):
            files.append(file)
        return files

