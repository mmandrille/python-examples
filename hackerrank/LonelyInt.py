'''
Given an array of integers, where all elements but one occur twice, find the unique element.
'''
def lonelyinteger(arr):
    # Write your code here
    # Generate counter dict and loadit
    counterDict = {}
    for n in arr:
        if n not in counterDict:
            counterDict[n] = 0
        counterDict[n] += 1
    # Get lonely
    for key, value in counterDict.items():
        if value == 1:
            return key            

if __name__ == '__main__':
    result = lonelyinteger([15, 60, 74, 1, 94, 93, 28, 48, 70, 98, 45, 94, 42, 45, 48, 1, 72, 9, 24, 93, 41, 70, 60, 28, 11, 20, 72, 35, 11, 98, 31, 74, 31, 41, 9, 42, 20, 35, 24])
    assert result == 15
    print("Success")