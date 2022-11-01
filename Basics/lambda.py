'''
In Python, an anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword in Python
  anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.
'''

# Simple usage:
add = lambda a, b: a + b
print(f"Simple Usage: {add(2,5)}")


# Complex:
def base_func(n):
    return lambda a: a * n


mydoubler = base_func(2)  # Define with a=2
mytripler = base_func(3)  # Define with a=3

print(f"Doubler Usage: {mydoubler(5)}")
print(f"Triple Usage: {mytripler(5)}")
