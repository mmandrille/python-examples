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
def create_consumer():
    while True:#loop infinito waiting till kafka is online
        try:
            consumer = KafkaConsumer(
                zconsts.KAFKA_TOPIC,
                bootstrap_servers=[zconsts.KAFKA_URL],
                #auto_offset_reset="earliest",
                #session_timeout_ms=60000,
                #heartbeat_interval_ms=5000,
                #enable_auto_commit=True,
                #group_id="1",
                value_deserializer=lambda msg: json.loads(msg.decode('utf-8'))
            )
            #if this succeed:
            logger.info("Begin reading Kafka Service in %s...", format(zconsts.KAFKA_URL))
            return consumer

        except:#If kafka not online
            time.sleep(zconsts.SLEEP_TIME)#we wait one more second
            logger.warning("Waiting for Kafka Service in %s...", format(zconsts.KAFKA_URL))