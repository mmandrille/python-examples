#Python import
import json
import time
import signal
import string
import random
import logging
from datetime import datetime
from logging import handlers
from queue import Empty as EmptyException
from multiprocessing import Process, Event, Queue
#Proyect import
from utils import constants as zconsts
from utils import functions as zfuncs

#Logging definition:
rotatorHandler = handlers.RotatingFileHandler(
    filename='logs/producer.log', 
    mode='a',
    maxBytes=1024*1024*10, #10mb
    backupCount=5,
    encoding=None,
    delay=0
)
logging.basicConfig(
    level=zconsts.LOGGING_LEVEL,#Change to DEBUG for more info in the constants
    format='%(asctime)s;%(process)s;%(name)s;%(levelname)s;%(message)s',
    datefmt="%y-%m-%d %H:%M:%S",
    handlers=[rotatorHandler, ],
)
logger = logging.getLogger("MainCode")

#Definition of global objects
msgQueue = Queue()

#Base Estructural code
def msg_generator(exit_event):
    count = 0
    while not exit_event.is_set():
        count += 1 #  to check and give some feedback
        # Generate a random msg:
        chars = ''.join([string.ascii_letters, string.digits])
        msg = {"message": ''.join([random.SystemRandom().choice(chars) for i in range(50)])} # Its a json(?
        #Add to queue
        msgQueue.put(msg)
        # Generate some delay
        time.sleep(zconsts.MSG_CREATION_DELAY_MS/1000) # sleep requiere seconds
        if count > zconsts.SCREENING_RATE:
            qsize = msgQueue.size()
            logging.info("%s put in queue, actual size: %s, %s items in %s", msg, qsize, count, (datetime.now() - check_time).total_seconds())
            if qsize > zconsts.MAX_QUEUE:
                logging.warn("Queue over max size, you should allow more workers!")
                time.sleep(zconsts.SLEEP_TIME)
            
            #Restart lap
            count, check_time = 0, datetime.now()

def msg_sender(queue, exit_event):
    count = 0
    generator_fail_count = 0
    producer = zfuncs.kafka_create_producer(zconsts.KAFKA_URL, zconsts.KAFKA_TOPIC)
    while not queue.empty() or not exit_event.is_set():
        try:
            # We try to get object from queue
            msg = msgQueue.get_nowait()
            generator_fail_count = 0 # If we fetch one, generator is working
            producer.send(zconsts.KAFKA_TOPIC, json.dumps(msg))
            # Some feedback
            count += 1
            if not count%zconsts.SCREENING_RATE:
                qsize = msgQueue.size()
                logging.info("%s sended to Kafka, Queue Size is %s", msg, qsize)
            
            
        except EmptyException:
            time.sleep(zconsts.WAIT_TIME)#We avoid overloading
            generator_fail_count+=1
            if generator_fail_count == 30:
                logging.warn("Queue Empty for %ss, something is going wrong with generator!", zconsts.WAIT_TIME * generator_fail_count)
                generator_fail_count == 0 # Reset Counter

        except Exception as e:
            logger.error(e, exc_info=True) # Error in processesing
        

def main():
    #Preparing multithreading
    processes = []
    exit_event = Event()
    # Kafka Create Topic:
    if zfuncs.kafka_create_topic(zconsts.KAFKA_URL, zconsts.KAFKA_TOPIC):
        logger.info("Kafka Online, Topic Created...")
    # Msg Generator
    process1 = Process(target=msg_generator, args=(exit_event, ))
    processes.append(process1)
    process1.start()
    # We'll define a default signal handler to be inherited by the child
    # we want the stream reader to use its own handler
    default_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    # Event consumers
    for i in range(zconsts.MAX_WORKERS):
        processor = Process(target=msg_sender, args=(msgQueue, exit_event))
        processes.append(processor)
        processor.start()
        logger.info("Worker initiated to consume messages: %s", i)#We logg the start

    # restoring signal handling
    signal.signal(signal.SIGINT, default_handler)
    try: 
        signal.pause()
    except KeyboardInterrupt:
        exit_event.set()

    # We need to do this busy wait here because python threads sometime hangs. 
    while not msgQueue.empty(): # So we'll terminate them when the queue is emptied
        logger.info("Waiting for queue to flush all msgs: %s remaining...", msgQueue.qsize())
        time.sleep(1)

    # We finish all the process
    for process in processes:
        process.terminate()
        process.join()

    logger.info("Program Finished...")

#Launch!
if __name__ == "__main__":
    #Run code
    main()