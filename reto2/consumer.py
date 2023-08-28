import json
import pika
import glob
import os
import datetime
from dotenv import load_dotenv
from configs import *

load_dotenv()
RMQ_HOST = os.getenv('RMQ_HOST')
RMQ_PORT = os.getenv('RMQ_PORT')
RMQ_USER = os.getenv('RMQ_USER')
RMQ_PASS = os.getenv('RMQ_PASS')

connection = pika.BlockingConnection(pika.ConnectionParameters(RMQ_HOST, RMQ_PORT, '/', pika.PlainCredentials(RMQ_USER, RMQ_PASS)))
channel = connection.channel()

def list_files(ch, method, properties, body):
    all_files_info = []
    for file in os.listdir(DIRECTORY):
        file_path = os.path.join(DIRECTORY, file)
        file_size = os.path.getsize(file_path)
        file_mtime = os.path.getmtime(file_path)
        file_mtime_datetime = datetime.datetime.fromtimestamp(file_mtime)
        formatted_mtime = file_mtime_datetime.strftime("%Y-%m-%d %H:%M:%S")
        all_files_info.append({"name":file, "size":file_size, "last_updated": formatted_mtime})
    print(all_files_info)
    publish_response(ch, method, properties, all_files_info)

def search_files(ch, method, properties, body):
    target_string = body.decode('utf-8')
    print("Searching products that match string: " + target_string)
    matched_files = []
    for file in os.listdir(DIRECTORY):
        if target_string in file:
            file_path = os.path.join(DIRECTORY, file)
            file_size = os.path.getsize(file_path)
            file_mtime = os.path.getmtime(file_path)
            file_mtime_datetime = datetime.datetime.fromtimestamp(file_mtime)
            formatted_mtime = file_mtime_datetime.strftime("%Y-%m-%d %H:%M:%S")
            matched_files.append({"name":file, "size":file_size, "last_updated": formatted_mtime})

    print(matched_files)
    publish_response(ch, method, properties, matched_files)

def publish_response(ch, method, properties, response):
    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id,
        ),
        body=json.dumps(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Response sent to RabbitMQ!")
    
channel.basic_consume(queue="queue1", on_message_callback=list_files, auto_ack=False)
channel.basic_consume(queue="queue2", on_message_callback=search_files, auto_ack=False)
channel.start_consuming()