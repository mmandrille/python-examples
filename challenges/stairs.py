'''
    There is a Stair with N steps. 
    In every step you could take one or two up.
    Create a fuction that calculate how many different ways of take the stair exists
'''
# steps n=5
#1# 0 1 2 3 4 5 
#2# 0 1 2 3 5
#3# 0 1 2 4 5
#4# 0 1 3 4 5
#5# 0 1 3 5
#6# 0 2 3 4 5
#7# 0 2 3 5
#8# 0 2 4 5

class RecursiveCounter():
    def __init__(self, max_steps):
        print("Running Recursive Approach:")
        self.counter = 0
        self.max = max_steps
        self.calc_recursive(0) # We are out of stair (to 1 or 2)
        print(f"There are {self.counter} possibilities with {self.max} max_steps")
    
    def calc_recursive(self, step):
        if step < self.max:
            self.calc_recursive(step+1) # Calculate one step
            self.calc_recursive(step+2) # Calculate other step
        elif step == self.max:
            self.counter+=1

# Run:
if __name__ == "__main__":
    icounter = RecursiveCounter(5)