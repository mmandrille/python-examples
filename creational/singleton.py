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
from datetime import datetime

# Classes Definition
class NamedSingletonObject(object):
    instances = {} # We will keep created instances here
    class __NamedSingletonObject():
        def __init__(self, name:str):
            self.name = name

        def __str__(self):
            return f"{self.name}({id(self)})"

    def __new__(cls, name):
        # Check if already exist
        print(f"\nWe are creating: {name} Singletone")
        if name not in cls.instances.keys():
            print(f"There is not a '{name}' singleton. Creating...")
            # Create if not
            cls.instances[name] = cls.__NamedSingletonObject(name)
        # Return correct singleton
        return cls.instances.get(name)

class Logger(NamedSingletonObject):
    """
    A file-based message logger with the following properties
    Attributes:
    file_name: a string representing the full path of the log file to which 
    this logger will write its messages
    """
    def __new__(self, filename):
        """Return a Logger object whose file_name is *file_name*"""
        super().__new__(self, filename)
        logger = self.instances.get(filename)
        logger.file_name = filename
        return logger

    def _write_log(self, level, msg):
        """Writes a message to the file_name for a specific Logger instance"""
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level}]-{datetime.now()} {msg}\n")
    
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

# Testing
if __name__ == '__main__':
    # We create 2 loggers
    log1 = Logger("primary.log")
    print(f"obj1: {log1.file_name} ({id(log1)})")
    
    log2 = Logger("secundary.log")
    print(f"obj1: {log1.file_name} ({id(log1)})")
    print(f"obj2: {log2.file_name} ({id(log2)})")

    print(f"\nWe check if are't the same object: {log1 is not log2}")
    assert True == (log1 is not log2)
    # We call Logger with same name:
    log3 = Logger("primary.log")
    print(f"We check if are the same object 1 & 3: {log1 is log3}")
    assert True == (log1 is log3)
    
