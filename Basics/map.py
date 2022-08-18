'''
    map() function receive a function and a iterable
    and returns a map object(which is an iterator) of the results after applying the given function to each item of the iterable (list, tuple etc.)
'''
def calculateSquare(n):
    return n*n

# Run our code
if __name__ == "__main__":
    numbers = (1, 2, 3, 4)
    map_result = map(calculateSquare, numbers)
    print(f"We obtain a map object: {map_result}\n")
    
    print("We can just transform it:")
    result = list(map_result)
    print(result)
    
    print(f"\nBut now the map_result is empty: {list(map_result)}")