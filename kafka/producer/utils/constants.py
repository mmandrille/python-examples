#python imports
import os
import logging

#Constants:
MSG_CREATION_DELAY_MS = int(os.getenv('MSG_CREATION_DELAY_MS', default=10))
LOGGING_LEVEL = int(os.getenv('LOGGING_LEVEL', default=logging.DEBUG))
MAX_QUEUE = int(os.getenv('MAX_QUEUE', default=5000))
WAIT_TIME = int(os.getenv('WAIT_TIME', default=30))
SLEEP_TIME = int(os.getenv('SLEEP_TIME', default=30))
MAX_WORKERS = int(os.getenv('MAX_WORKERS', default=4))
SCREENING = os.getenv('PYTHON_SCREENING', default=True)
SCREENING_RATE = int(os.getenv('SCREENING_RATE', default=5000))

#kafka
KAFKA_URL = os.getenv('KAFKA_URL', default='localhost:9092') # This is with: docker-compose -f docker-compose.yml up broker
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', default='testing')