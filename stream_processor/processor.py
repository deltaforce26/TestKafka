import pymongo, json
from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError

words = ['hostage', 'explos']

consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers='localhost:19092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
)


producer = KafkaProducer(
    bootstrap_servers='localhost:19092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))


print("Listening for messages on Kafka.")


def consume_messages():
    for message in consumer:
        data = message.value
        write_to_mongo(data)
        produce_to_explosive(data)



def produce_to_hostage(message):
    try:
        print(f"Sending data: {message}")
        producer.send('messages.hostage', value=message)
        producer.flush()
    except KafkaError as e:
        print(f"Kafka error: {e}")



def produce_to_explosive(message):
    try:
        print(f"Sending data: {message}")
        message.pop('_id')
        producer.send('messages.explosive', value=message)
        producer.flush()
    except KafkaError as e:
        print(f"Kafka error: {e}")



def check_message(message):
    sentences = message['sentences']
    res = list(map(lambda x: any(map(lambda y: y in x.split(),
                                     words)), sentences))
    return True in res


# n = s.count(word)
# if n > 0:
#



def write_to_mongo(message):
    col = connect_to_mongo()
    col.insert_one(message)
    print(f"Inserted message: {message}")



def connect_to_mongo():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print('connected to mongodb.')
    messages_db = client['messages_db']
    all_messages = messages_db['all_messages']
    return all_messages



if __name__ == '__main__':
    while True:
        consume_messages()







'''
{
     "email": "jeremy37@example.org",
     "username": "jonesalejandra",
     "ip_address": "215.67.111.124",
     "created_at": "2024-10-15T05:29:13.450066",
     
     
     "location": {
         "latitude": 8.5478895,
         "longitude":-135.24204,
         "city": "Port Josephburgh",
         "country": "PA"
     },
     
     "device_info": {
     "browser": "Mozilla/5.0",
     "os": "iOS",
     "device_id": "c4a3ce0d-4f4f-4bc9-9e94-b135e32cfe81"
     },
     
     "sentences": [
     "Public quickly spend hear sing.",
     "Difference nothing environmental shake decide.",
     "Natural southern what nice."
     ]
}
 '''