#Python imports
import sys
import json
import time
import asyncio
import logging
from logging import handlers
from datetime import datetime
#Proyect imports
from utils.classes import StatusClass
from utils import constants as zconsts
from utils import functions as zfuncs


#Logging definition:
rotatorHandler = handlers.RotatingFileHandler(
    filename='logs/certprocessor.log', 
    mode='a',
    maxBytes=10*1024*1024,
    backupCount=5,
    encoding=None,
    delay=0
)
logging.basicConfig(
    level=zconsts.LOGGING_LEVEL,#Change to DEBUG for more info in the constants
    format='%(asctime)s;%(process)s;%(name)s;%(levelname)s;%(message)s',
    datefmt="%Y%m%d;%H:%M:%S",
    handlers=[rotatorHandler, ],
)
logger = logging.getLogger("certprocessor.MainCode")

#Definition of process
async def process_msgs(status):
    # Monitoring
    logger.info('queue_reader started...')
    count=0
    check_time = datetime.now()                        
    #We start reading messages from kafka:
    while True:
        try:
            # Read from Kafka Topic
            msg = status.kafka_consumer.poll(timeout=1.0)
            # Check message
            if msg:
                # We fetch a msg from kafka topic
                asyncio.sleep(zconsts.MSG_PROCESING_DELAY_MS/1000) # Simulate async slow task
                #some data sent to screen so we know is working xD
                if zconsts.SCREENING:
                    count+=1
                    if count > zconsts.SCREENING_RATE:
                        logger.info("{0} Readed from Topic:{1}. Processed {2} in {3} secs",
                                    msg["message"],
                                    zconsts.KAFKA_TOPIC,
                                    count,
                                    (datetime.now() - check_time).total_seconds()
                                )
                        #Restart lap
                        count, check_time = 0, datetime.now()

            else: # Kafka topic is empty
                await asyncio.sleep(zconsts.SLEEP_TIME) # we make time of cpu for others process
        except Exception as e:
            logger.error('Uknown Fail receiving msg from kafka: %s', e, exc_info=sys.exc_info())

def main():
    status = StatusClass() # Instance Global Administrator
    #Instance general loop
    loop = asyncio.get_event_loop()
    #We create async tasks
    for x in range(zconsts.MAX_TASKS):
        loop.create_task(process_msgs(status))
        logger.info('{0}/{1} tasks created...'.format(x, zconsts.MAX_TASKS))
    #We make the work generator start
    loop.run_forever()

#Launch time!
if __name__ == "__main__":
    main() # Run code
