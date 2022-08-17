'''
Given an integer n, print the following values for each integer from 1 to n:
1- Decimal
2- Octal
3- Hexadecimal (capitalized)
4- Binary

Function Description
Complete the print_formatted function in the editor below.

print_formatted has the following parameters:
    int number: the maximum value to print

Prints
    The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format
    A single integer denoting .
'''

def print_formatted(number):

    binLen = len(bin(number).removeprefix('0b'))
    
    for num in range(1,number+1):
        print(
            " ".join(
                [
                    str(num).rjust(binLen),
                    oct(num)[2:].rjust(binLen),
                    hex(num)[2:].upper().rjust(binLen),
                    bin(num)[2:].rjust(binLen)
                ]
            )
        )
        
        
if __name__ == '__main__':
    n = int(input("Insert Lines to print: "))
    print_formatted(n)