'''
Tenes un vector con las temperaturas de cada día.
Por ejemplo: [20, 23, 22, 20, 19, 24, 24]
Qué algoritmo implementarías para saber, para cada día, cuantos días tenes que esperar para que la temperatura sea mayor o igual a la de ese día.
El vector de salida pra el ejemple debería ser [1, 4, 3, 2, 1, 0]
En caso de que no haya un dia de mayor temperatura devolver 0.
'''
#package imports

# Definitions
weather = [20, 23, 22, 20, 19, 24, 24]
expected = [1, 4, 3, 2, 1, 1, 0]

# Define our dict
class TempsDict(dict):
    def add_day(self, day, temp):
        if temp not in self:
            self[temp] = []
        self[temp].append(day)
    
    def get_higher(self, day, temp):
        valid = set()
        [
            [
                valid.add(d-day) for d in self[t] if d>day # 2. We only add the higher days (No itself)
            ] for t in [
                t for t in self.keys() if t>=temp # 1. We get all temps higher or equal to param
            ]
        ]
        try:
            return min(valid)
        except:
            return 0

# Run:
if __name__ == "__main__":
    print(f"Weather is: {weather}")
    print(f"We expected: {expected}")
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
    assert response == expected
    print("Success")