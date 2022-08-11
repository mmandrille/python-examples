# Python imports
import json
import sys
import time
import asyncio
import logging
#Imports extras:
from kafka import KafkaConsumer
# Proyect Imports
from utils import constants as zconsts

# Initializations
logger = logging.getLogger("Functions")

# Our functions
def create_consumer(process_id):
    while True: # eternal loop waiting till kafka is online
        try:
            consumer = KafkaConsumer(
                zconsts.KAFKA_TOPIC,
                bootstrap_servers=[zconsts.KAFKA_URL],
                # group_id="1",
                # session_timeout_ms=60000,
                # enable_auto_commit=True,
                # auto_offset_reset='beginning',
                value_deserializer=lambda v: json.loads(v.decode("utf-8"))
            )
            #if this succeed:
            logger.info("Consumer-%s Begin reading Kafka Broker in %s...", process_id, zconsts.KAFKA_URL)
            return consumer

        except Exception as e:#If kafka not online
            time.sleep(zconsts.SLEEP_TIME)#we wait one more second
            logger.warning("Waiting for Kafka Broker in %s.\n%s", zconsts.KAFKA_URL, e)