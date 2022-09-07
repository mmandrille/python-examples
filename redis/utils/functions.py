# Python imports
import time
import hashlib
#Package import
import redis
#Proyect import
from utils import constants as zconsts

# Functions definition
def fetch_from_db(key):
    # In this function we will simulate a slow database query
    time.sleep(zconsts.FAKE_DELAY)
    # Return hashed key
    return str(hashlib.md5(key.encode("utf-8")))

def get_cache_client():
    return redis.Redis(host=zconsts.REDIS_URL, port=zconsts.REDIS_PORT)

def get_cached_object(CacheClient, key):
    message = CacheClient.get(key)
    if not message:
        # we dont have it on cache, we will have to look for it to Database:
        message = fetch_from_db(key)
        # After fetching we store it on cache:
        CacheClient.set(key, message)
    # At this point we have the message
    return message