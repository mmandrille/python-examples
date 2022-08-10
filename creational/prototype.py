""" The Prototye Pattern

Notes:

In the prototype pattern, rather than creating new instances of an object, only
one instance (the breeder) of a class (the prototype) is created and deep-copied
whenever the need arises. This pattern is particularly useful when:

+ The cost of initialization is high.
+ Many objects of the same type are needed but some (or all) properties that are
    costly (time/space/bandwidth) to set remain the same across all objects.
    
This example will be based on Practial Python Design Patterns by Wessel Badenhorst

"""
# Requiered imports
import json
from copy import deepcopy
from abc import ABCMeta, abstractmethod

# Classes
class UnitsDict(dict):
    def add_unit(self, unit):
        if unit.unit_type not in self:
            self[unit.unit_type] = {}        
        self[unit.unit_type][unit.lvl] = unit

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass

class Concrete(Prototype):
    def clone(self):
        return deepcopy(self)

class Unit(Prototype):
    def __init__(self, name:str, lvl:int, stats:dict):
        self.unit_type = name
        self.lvl = lvl
        for key, value in stats.items():
            setattr(self, key, value) # We generate a atribute with every item in the data dict
    
    def __str__(self):
        return f"{self.unit_type} ({self.lvl})"

    def clone(self):
        return deepcopy(self)

class Knight(Unit):
    pass # Define special methods

class Archer(Unit):
    pass # Define special methods

class Priest(Unit):
    pass # Define special methods

class Barracks(object):
    def __init__(self, player):
        owner = player
        data = json.loads(open("resources/units.json").read()) # Load Units Config File
        self.units = UnitsDict()# Here we will create all units
        # Available units, (This could change depending on the player)
        self.available_types = {
            "Knight": Knight,
            "Archer": Archer,
            "Priest": Priest # Still not implemented on resources/units.json
        }
        # We loop though units creating them:
        for type, UnitClass in self.available_types.items():
            # We fetch all defined items from that class
            TypeLevels = data.get(type, {}) # Avoid NoneType Error in the next for
            # We create a class for every Stat Block
            for lvl, stats in TypeLevels.items(): # Loop every block stat
                self.units.add_unit(
                    self.available_types[type] # We call the constructor
                    (
                        type, #Name
                        int(lvl), # Lvl is String in Json
                        stats # Dict with stats
                    ) 
                )
    
    def build_unit(self, unit_type, level):
        return self.units[unit_type][level].clone()

if __name__ == "__main__":
    barracks = Barracks("nickname") # On the instancing we already create the prototypes
    knight1 = barracks.build_unit("Knight", 1)
    archer1 = barracks.build_unit("Archer", 2)
    print(f"[knight1] {knight1}")
    print(f"[archer1] {archer1}")
    assert knight1.Life == 400
    assert archer1.AttackRange == 12