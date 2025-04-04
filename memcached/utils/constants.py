#python imports
import os
import logging

#Constants:
DEBUG_LEVEL = int(os.getenv('DEBUG_LEVEL', default=logging.INFO))
TTL_CACHE = int(os.getenv('TTL_CACHE', default=14400))
FAKE_DELAY = int(os.getenv('FAKE_DELAY', default=5))
TIMES = int(os.getenv('TIMES', default=25))
TIME_OUT = int(os.getenv('TIME_OUT', default=60))
# Mem Cache
MEMCACHE_URL = os.getenv('MEMCACHE_URL', default='127.0.0.1:11211')