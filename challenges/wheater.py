'''
Tenes un vector con las temperaturas de cada día.
Por ejemplo: [20, 23, 22, 20, 19, 24, 24]
Qué algoritmo implementarías para saber, para cada día, cuantos días tenes que esperar para que la temperatura sea mayor o igual a la de ese día.
El vector de salida pra el ejemple debería ser [1, 4, 3, 2, 1, 0]
En caso de que no haya un dia de mayor temperatura devolver 0.
'''
#package imports
from queue import Queue

# Definitions
weather = [20, 23, 22, 20, 19, 24, 24, 21]
expected = [1, 4, 3, 2, 1, 1, 0, 0]

# Define our dict
class TempsDict(dict):
    def add_day(self, day, temp):
        if temp not in self:
            self[temp] = []
        self[temp].append(day)
    
    def get_higher(self, day, temp):
        # Example of self: {20: [0, 3], 23: [1], 22: [2], 19: [4], 24: [5, 6]}
        valids = set()
        [
            [
                valids.add(d-day) for d in self[t] if d>day # 2. We only add the higher days (No itself)
            ] for t in (
                t for t in self.keys() if t>=temp # 1. We get all temps higher or equal to param
            )
        ]
        # Conditional return
        return min(valids) if valids else 0

# Run:
if __name__ == "__main__":
    print(f"Weather is: {weather}")
    print(f"We expected: {expected}")
    
    print("First Attempt:")
    # Generate dict --> First loop
    temp_dict = TempsDict()
    for idx in range(len(weather)):
        temp_dict.add_day(idx, weather[idx])
    print(f"Dict Generated: {temp_dict}")
    # Resolve:
    response = []
    for idx in range(len(weather)):
        response.append(temp_dict.get_higher(idx, weather[idx]))
    # Check result
    print(f"Checking Response: {response}")
    assert response == expected
    print("Success:\n")
    
    print("Second Attempt:")
    # We will use a Stack
    stack = Queue() # FIFO stack
    response = []
    max = 0
    # Weather is: [20, 23, 22, 20, 19, 24, 24]
    for idx in range(len(weather)): # First loop
        # if higher We load the stack
        if not stack or (weather[idx] >= max): # If no stack or temp is higher than last
            max = weather[idx] # We save max value
            # We load it on stack
            stack.put((weather[idx],idx)) # Keep loading
            print(f"We loaded items to stack: {stack.queue}, results: {response}")
            # We generate results:
            last = stack.get()
            for d in range(last[1]-len(response))[::-1]:
                response.append(d+1)
                print(f"We fetch: {last}, we need to add {last[1]-len(response)} items")
    # We need to append 0 to not responded ones:
    response += [0] * (len(weather) - len(response))
    # Check result
    print(f"Checking Response: {response}")
    assert response == expected
    print("Success:\n")