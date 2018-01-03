from kafka import KafkaConsumer

server = '10.7.0.123:19092'

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=[server],
    consumer_timeout_ms=1000,
    auto_offset_reset='earliest',
    enable_auto_commit=False
)

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print(f'{message.topic}:{message.partition}:{message.offset}: key={message.key} value={message.value}')

# consume json messages
# KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

# consume msgpack
# KafkaConsumer(value_deserializer=msgpack.unpackb)

