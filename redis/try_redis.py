#Python import
import time
from datetime import datetime
#Proyect import
from utils import constants as zconsts
from utils import functions as zfuncs

#Launch!
if __name__ == "__main__":
    key = "Testing"
    # Instance MemCache client for every cert_sender process
    CacheClient = zfuncs.get_cache_client() # This could be in a lot of places of a project
    CacheClient.delete(key) # To avoid already existing key
    # Run testing
    performance = {}
    for x in range(zconsts.TIMES):
        check_time = datetime.now()
        zfuncs.get_cached_object(CacheClient, key) # We fetch our item
        performance[x] = (datetime.now() - check_time).total_seconds()
        
    # Show some results
    print("Results:")
    print(f"First time took {performance[0]:.4f}s fetching from database")
    print("At this point we set the key on Cache to retrieve value from there\n")
    print(f"All the next {zconsts.TIMES-1} fetchs should be faster")
    for idx in range(1, zconsts.TIMES):
        print(f"{idx} time\t Took {performance[idx]:.4f}s fetching from Cache")