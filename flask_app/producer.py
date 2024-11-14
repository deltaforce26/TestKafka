import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(
    bootstrap_servers='localhost:19092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))


def produce_to_kafka(email):
    try:
        print(f"Sending data: {email}")
        producer.send('messages.all', value=email)
        producer.flush()
    except KafkaError as e:
        print(f"Kafka error: {e}")
