# Python imports}
import json
import time
import logging
from logging import handlers
# Package imports
from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable, TopicAlreadyExistsError
# Project imports
from . import constants as zconsts

#Logging definition:
logger = logging.getLogger("Functions")

# Define functions
def kafka_create_topic(KAFKA_URL, TOPIC_NAME):
    while True:
        try:
            admin_client = KafkaAdminClient(
                bootstrap_servers=KAFKA_URL,
            )
            topic_list = [
                NewTopic(
                    name=TOPIC_NAME,
                    num_partitions=zconsts.KAFKA_PARTITIONS,
                    replication_factor=1
                ),
            ]
            admin_client.create_topics(new_topics=topic_list, validate_only=False)
            return True

        except NoBrokersAvailable:
            logger.warning("Kafka not online in: %s, waiting...", KAFKA_URL)
            time.sleep(1) # We wait to avoid overloading
        
        except TopicAlreadyExistsError:
            return True
            

def kafka_create_producer(KAFKA_URL, TOPIC_NAME):
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=[KAFKA_URL],
                value_serializer=lambda x: json.dumps(x).encode('utf-8'),
            )
            logger.debug("Producer instanced on: %s", KAFKA_URL)
            return producer
        except NoBrokersAvailable:
            logger.warning("Kafka not online in: %s, waiting...", KAFKA_URL)
            time.sleep(1) # We wait to avoid overloading