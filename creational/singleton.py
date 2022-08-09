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

class SingletonObject(object):
    class __SingletonObject():
        def __init__(self):
            self.val = None
        
        def __str__(self):
            return "{0!r} {1}".format(self, self.val)
    # the rest of the class definition will follow here, as per the previous logging script
    instance = None

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

if __name__ == '__main__':
    obj1 = SingletonObject()
    obj1.val = "Object value 1"
    print("print obj1: ", obj1)
    print("-----")
    obj2 = SingletonObject()
    obj2.val = "Object value 2"
    print("print obj1: ", obj1)
    print("print obj2: ", obj2)
