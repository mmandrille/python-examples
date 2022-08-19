'''
    There is a Stair with N steps. 
    In every step you could take one or two steps up.
    Create a fuction that calculate how many different ways of take the stair exists
'''
# Imports
from functools import lru_cache

# Definitions
class RecursiveClimber():
    def __init__(self, height):
        self.ways = 0
        self.height = height
        self.calc_recursive(0) # We are out of stair (to 1 or 2)
        print(f"RecursiveClimber: There are {self.ways} possibilities with {height} max_steps")
    
    # Here we utilize recursive executions
    def calc_recursive(self, step):
        if step < self.height:
            self.calc_recursive(step+1) # climb one step
            self.calc_recursive(step+2) # climb other step
        elif step == self.height:
            # Every time we get to heigh on a way, we increase ways
            self.ways+=1 # Basicaly we will generate a recursion for every possible way

def countWays(height):
    steps = [0] * (height + 1) # We generate one position for every lvl of the stair
    steps[0] = 0 # at no height no steps
    steps[1] = 1 # only one step height, only one step
    steps[2] = 2 # only two options at max 2 steps (1-1 and 2)
 
    for i in range(3, height+1): # We will calculate all the heights
        steps[i] = steps[i-2] + steps[i-1] # every lvl possibilities its the sum of previous two
 
    print(f"countSteps: There are {steps[height]} possibilities with {height} max_steps")
    return steps[height]

# Run:
if __name__ == "__main__":
    stair_levels = 32
    cs = countWays(stair_levels)
    rc = RecursiveClimber(stair_levels) # Much slower
    # Check all resolve the same
    assert rc.ways == cs