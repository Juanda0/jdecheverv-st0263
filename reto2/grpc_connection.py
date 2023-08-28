import grpc
from configs import *
import service_pb2, service_pb2_grpc

class grpc_connection:
    def __init__(self):
        self.channel = grpc.insecure_channel(GRPC_HOST)
        self.client = service_pb2_grpc.fileServiceStub(self.channel)

    def search_files(self, file_name):
        files = []
        for response_stream in self.client.SearchFiles(service_pb2.File(fileName=file_name)):
            for file in response_stream.files:
                files.append({"name": file.name, "last_updated":file.lastUpdated, "size":file.size})
        return files

    def list_files(self):
        files = []
        for response_stream in self.client.ListAllFiles(service_pb2.Empty()):
            for file in response_stream.files:
                files.append({"name": file.name, "last_updated":file.lastUpdated, "size":file.size})
        return files

