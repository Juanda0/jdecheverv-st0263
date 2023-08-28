import grpc
import os
import datetime
from concurrent import futures
import service_pb2, service_pb2_grpc
from configs import *

class FileService(service_pb2_grpc.fileServiceServicer):
   
   def SearchFiles(self, request, context):
      target_string = request.fileName
      print("Searching products that match string: " + target_string)
      matched_files = []
      for root, _, files in os.walk(DIRECTORY):
        for file in files:
            if target_string in file:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_mtime = os.path.getmtime(file_path)
                matched_files.append(service_pb2.singleFileResponse(name = file, lastUpdated = file_mtime, size = file_size))
      yield service_pb2.multipleFilesResponse(files=matched_files)

   def ListAllFiles(self, request, context):
      print("Listing all files")
      all_files_info = []
      for file in os.listdir(DIRECTORY):
            print(file)
            file_path = os.path.join(DIRECTORY, file)
            file_size = os.path.getsize(file_path)
            file_mtime = os.path.getmtime(file_path)
            print(1)
            file_mtime_datetime = datetime.datetime.fromtimestamp(file_mtime)
            formatted_mtime = file_mtime_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print(file, formatted_mtime, file_size)
            all_files_info.append(service_pb2.singleFileResponse(name = file, lastUpdated = formatted_mtime, size = file_size))
      print(all_files_info)
      yield service_pb2.multipleFilesResponse(files=all_files_info)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_fileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port(GRPC_RULE)
    print("Service running at port:", GRPC_RULE)
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()