#python import
import time
import json
from datetime import datetime
#Package import
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
#Proyect import
from utils.constants import KAFKA_URL, KAFKA_TOPIC

# Base code:
def main():
    #Preparing multithreading
    processes = []
    exit_event = Event()
    # Kafka Create Topic:
    if zfuncs.kafka_create_topic(zconsts.KAFKA_URL, zconsts.KAFKA_TOPIC):
        logger.info("Kafka Online, Topic Created...")

#Code
if __name__ == '__main__':
    

ready = False
#Preparate kafka Producer
while not ready:
    try:
        producer = KafkaProducer(
                bootstrap_servers=KAFKA_URL,
                value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            )
        print("Begin sending Kafka Service in {0}...".format(KAFKA_URL))
        ready = True
    except NoBrokersAvailable:
        time.sleep(1)#Esperamos un segundo mas
        print("Waiting for Kafka Service in {0}...".format(KAFKA_URL))

#Send staff
for counter in range(CANT_TESTS):
    msg = {
        'time': str(datetime.now()),
        'counter': counter,
    }
    send_status = producer.send(KAFKA_TOPIC, msg)
    print('{0} msgs sent to {1}>{2}...'.format(counter, KAFKA_URL, KAFKA_TOPIC))