#Python imports
import logging
#Project imports
from  utils import functions as zfuncs

#Instance Code
logger = logging.getLogger("Classes")

#class definitions
class StatusClass:
    def __init__(self):
        self.msgs = []
        self.kafka_consumer = zfuncs.create_consumer()