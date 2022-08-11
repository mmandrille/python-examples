#python imports
import os
import logging

#Constants:
MSG_PROCESING_DELAY_MS = int(os.getenv('MSG_PROCESING_DELAY_MS', default=250))
LOGGING_LEVEL = int(os.getenv('LOGGING_LEVEL', default=logging.DEBUG))
MAX_QUEUE = int(os.getenv('MAX_QUEUE', default=5000))
SLEEP_TIME = int(os.getenv('SLEEP_TIME', default=1))
WAIT_TIME = int(os.getenv('WAIT_TIME', default=30))
MAX_TASKS = int(os.getenv('MAX_TASKS', default=4))
SCREENING = os.getenv('PYTHON_SCREENING', default=True)
SCREENING_RATE = int(os.getenv('SCREENING_RATE', default=500))

#kafka
KAFKA_URL = os.getenv('KAFKA_URL', default='localhost:29092') # This is with: docker-compose -f docker-compose.yml up broker
KAFKA_TOPIC = os.getenv('KAFKA_TOPIC', default='testing')