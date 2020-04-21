from kafka import KafkaProducer
bootstrap_servers = ['localhost:9092']
topicName = 'topic1'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
ack = producer.send(topicName, b'hello')

metadata = ack.get()
print(metadata.topic)
print(metadata.partition)
producer = KafkaProducer(bootstrap_servers=bootstrap_servers, retries=5, value_serializer=lambda m: json.dumps(m).encode('ascii'))



