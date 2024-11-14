import json
from kafka import KafkaConsumer
from db.models import MessageModel, DeviceModel, LocationModel, SentenceModel
from db.repository.message_repo import insert_model

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
        device = DeviceModel(
            browser=data.get('browser'),
            os=data.get('os'),
            device_id=data.get('device_id'),
        )
        device_id = insert_model(device)
        message = MessageModel(
            email=data.grt('email'),
            username=data.get('username'),
            ip_address=data.get('ip_address'),
            created_at=data.get('created_at'),
            device_id=device_id
        )
        message_id = insert_model(message)
        location = LocationModel(
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            city=data.get('city'),
            country=data.get('country'),
            message_id=message_id
        )
        insert_model(location)
        sentences = SentenceModel(
            sentences=data.get('sentences'),
            message_id=message_id
        )
        insert_model(sentences)



if __name__ == '__main__':
    while True:
        consume_messages()

