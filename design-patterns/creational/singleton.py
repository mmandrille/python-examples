""" The Singleton Pattern

Notes:

While there are multiple ways to implement the Singleton pattern, the point of
the Singleton pattern is to expose only one object without the possiblity to
create multiple _instances of the object.

It is important to note that if your need for this design pattern can be met by
a simple class-less python module (within a .py file), that solution is simpler and
usually preferable. One limitation of using a module's namespace instead of a Singleton
is that a module cannot be constructed with arguments and cannot have properties. 

Extra:
I strongly recommend the 'Borg' pattern as a more elegant alternative (see borg.py). It
usually meets all the needs of a Singleton with a more classical OOP approach.

"""
# Import definition
import os
from datetime import datetime

# Classes Definition
class Logger(object):
    """
    A file-based message logger with the following properties
    Attributes:
    file_name: a string representing the full path of the log file to which 
    this logger will write its messages
    """
    __instances = {} # We will keep created instances here

    class __LoggerObject():
        def __init__(self, filename:str):
            self.filename = filename
        def __str__(self):
            return f"{self.filename}({id(self)})"
        # Working Methods
        def _write_log(self, level, msg):
            """Writes a message to the file_name for a specific Logger instance"""
            with open(self.filename, "a") as log_file:
                log_file.write(f"[{level}]-{datetime.now()} {msg}\n")

        def delete(self):
            os.remove(self.filename)

        # We define a method for every level, we could need specific treatments
        def critical(self, msg):
            self._write_log("CRITICAL",msg)
        def error(self, msg):
            self._write_log("ERROR", msg)
        def warn(self, msg):
            self._write_log("WARN", msg)
        def info(self, msg):
            self._write_log("INFO", msg)
        def debug(self, msg):
            self._write_log("DEBUG", msg)

    def __new__(cls, filename):
        """Return a Logger object whose filename is *filename*"""
        if filename not in cls.__instances.keys():
            cls.__instances[filename] = cls.__LoggerObject(filename)
        return cls.__instances[filename]       

# Testing
if __name__ == '__main__':
    # We create 2 loggers
    log1 = Logger("primary.log")
    print(f"obj1: {log1.filename} ({id(log1)})")
    
    log2 = Logger("secundary.log")
    print(f"obj1: {log1.filename} ({id(log1)})")
    print(f"obj2: {log2.filename} ({id(log2)})")

    print(f"\nWe check if are't the same object: {log1 is not log2}")
    assert (log1 is not log2)
    # We call Logger with same name:
    log3 = Logger("primary.log")
    print(f"We check if are the same object 1 & 3: {log1 is log3}")
    assert (log1 is log3)
    
    # Check its working:
    log1.debug("testing file creation")
    assert os.path.exists(log1.filename)
    log1.delete()
    assert not os.path.exists(log1.filename)
    
    
    
