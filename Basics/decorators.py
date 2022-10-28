# importing libraries
import time
import math


# decorator to calculate duration
def calculate_time(name):
    print(f"Calculating time for: {name}")

    def Inner(func):
        # added arguments inside the wrapper,
        # if function takes any arguments can be added like this:
        def wrapper(*args, **kwargs):
            # storing time before function execution
            begin = time.time()
            # We execute our function
            func(*args, **kwargs)
            # Show time after
            print(f"Total time for {name} was: {time.time() - begin:.2f}s")

        # This is the moment when the subfunction is called
        return wrapper
    return Inner  # This is the first execution and receive func as parameter


@calculate_time(name="factorial")  # this can be added to any function
def factorial(num):
    time.sleep(1)  # We add some delay so its looks cooler xD
    print(f"Factorial of {num} is: {math.factorial(num)}")


# Run our code
if __name__ == "__main__":
    factorial(10)
