import json
from kafka import KafkaConsumer



consumer = KafkaConsumer(
    'messages.explosive',
    bootstrap_servers='localhost:19092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    group_id='explosive-group'
)

print("Listening for messages on Kafka.")


def consume_messages():
    for message in consumer:
        data = message.value
