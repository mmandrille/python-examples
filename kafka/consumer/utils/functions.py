# Python imports
import time
import logging
from logging import handlers
# Package imports
from kafka import admin
# Project imports
import utils.constants as zconsts

#Logging definition:
rotatorHandler = handlers.RotatingFileHandler(
    filename='logs/functions.log', 
    mode='a',
    maxBytes=1024*1024*10, #10mb
    backupCount=1,
    encoding=None,
    delay=0
)
logging.basicConfig(
    level=zconsts.LOGGING_LEVEL,#Change to DEBUG for more info in the constants
    format='%(asctime)s;%(process)s;%(name)s;%(levelname)s;%(message)s',
    datefmt="%y-%m-%d %H:%M:%S",
    handlers=[rotatorHandler, ],
)
logger = logging.getLogger("Producer.Functions")

# Define functions
def kafka_create_topic(kafka_url, topic_name):
    while True:
        try:
            BROKER_URL = "PLAINTEXT://{0}".format(kafka_url)
            
            client = admin.AdminClient(
                {
                    "bootstrap.servers": BROKER_URL,
                    "queue.buffering.max.messages": 1000000, # 1M regs max buffer
                    "queue.buffering.max.kbytes": 4194304, # 4gb max buffer
                    "log.connection.close": False,
                }
            )
            
            topic_metadata = client.list_topics(timeout=5)
            topics = set(t.topic for t in iter(topic_metadata.topics.values()))
            # Check if topic exist:
            if topic_name in topics:
                print('Topic Already exist!')
                return True
            else:
                topics = [
                    admin.NewTopic(
                        topic=topic_name,
                        num_partitions=10,
                        replication_factor=1,
                        config={
                            "cleanup.policy": "delete",
                            "compression.type": "lz4",
                            "delete.retention.ms": "14400000", # 4 hours
                            "file.delete.delay.ms": "300000",
                            "retention.bytes": "21474836480", # 20Gb
                            "retention.ms": "14400000",
                        },
                    )
                ]
                futures = client.create_topics(topics)
                for topic, future in futures.items():
                    try:
                        future.result()
                        return True
                    except Exception as e:
                        print(f"failed to create topic {topic_name}: {e}")
                        time.sleep(1)
        except Exception as e:
            print(f"Failed connecting to broker")
            time.sleep(1)