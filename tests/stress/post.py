import pika
credentials = pika.PlainCredentials("admin", "admin")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.56.11",
                                     credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')

for each in range(10000000):
    channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

connection.close()
