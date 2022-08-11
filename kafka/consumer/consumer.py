#Python imports
import sys
import json
import time
import asyncio
import logging
from logging import handlers
from datetime import datetime
# Package Imports
from kafka.errors import KafkaError
#Proyect imports
from utils import constants as zconsts
from utils import functions as zfuncs

# Avoid Kafka Flooding
kafka_logger = logging.getLogger('kafka')
kafka_logger.setLevel(logging.WARN)

#Logging definition:
rotatorHandler = handlers.RotatingFileHandler(
    filename='logs/certprocessor.log', 
    mode='w', # This will start a clean log file
    maxBytes=10*1024*1024,
    backupCount=1,
    delay=False
)

logging.basicConfig(
    level=zconsts.LOGGING_LEVEL,#Change to DEBUG for more info in the constants
    format='[%(asctime)s;%(process)s;%(name)s;%(levelname)s] %(message)s',
    datefmt="%Y%m%d;%H:%M:%S",
    handlers=[rotatorHandler, logging.StreamHandler()],
)

logger = logging.getLogger("Main")
#Definition of process
async def process_msgs(process_id):
    # Monitoring
    logger.info('queue_reader-%s started...', process_id)
    count=0
    check_time = datetime.now()                        
    #We start reading messages from kafka:
    kafka_consumer = zfuncs.create_consumer()
    for msg in kafka_consumer:
        try:
            if msg:
                await asyncio.sleep(zconsts.MSG_PROCESING_DELAY_MS/1000) # Simulate async slow task
                #some data sent to screen so we know is working xD
                count+=1
                if count > zconsts.SCREENING_RATE:
                    logger.info(
                        "%s Readed from Topic:%s. Processed %s in %s secs",
                        msg.value,
                        zconsts.KAFKA_TOPIC,
                        count,
                        (datetime.now() - check_time).total_seconds()
                    )
                    #Restart lap
                    count, check_time = 0, datetime.now()
            else:
                await asyncio.sleep(zconsts.SLEEP_TIME)

        except KafkaError as e:
            logger.warning('\nKafka Error: %s', e)

        except Exception as e:
            logger.error("Error receiving msg from kafka: %s", e, exc_info=sys.exc_info())

        # we make time of cpu for processeing certs every lap
        await asyncio.sleep(0)

def main():
    #Instance general loop
    loop = asyncio.get_event_loop()
    #We create async tasks
    for x in range(zconsts.MAX_TASKS):
        loop.create_task(process_msgs(x))
        logger.info('{0}/{1} tasks created...'.format(x, zconsts.MAX_TASKS))
    #We make the work generator start
    loop.run_forever()

#Launch time!
if __name__ == "__main__":
    main() # Run code
