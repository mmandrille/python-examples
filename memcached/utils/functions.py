# Python imports
import time
import string
import hashlib
#Package import
from pymemcache import serde
from pymemcache.client import base as base_memcache
#Proyect import
from utils import constants as zconsts

# Functions definition
def fetch_from_db(key):
    # In this function we will simulate a slow database query
    time.sleep(zconsts.FAKE_DELAY)
    # Return hashed key
    return str(hashlib.md5(key.encode("utf-8")))

def get_cache_client():
    return base_memcache.Client(zconsts.MEMCACHE_URL, serde=serde.pickle_serde)

def get_cached_object(CacheClient, key):
    message = CacheClient.get(key, None)
    if not message:
        # we dont have it on cache, we will have to look for it to Database:
        message = fetch_from_db(key)
        # After fetching we store it on cache:
        CacheClient.set(key, message)
    # At this point we have the message
    return message