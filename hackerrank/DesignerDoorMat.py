'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be n.m (n is an odd natural number, and m is 3 times n.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
'''


height =  int(input("Insert Height of Door Mat: 13"))
widht = height * 3
# Some calculations
middle_line = int((height-1)/2)
max_draw = height - 2 # I dont really know if its a rule xD
pattern = ".|."

# Drawing:
for lvl in range(height):
    # Before center:
    if lvl < middle_line:
        items = 1+(2 * lvl)
        print(f'{items*pattern}'.center(widht,"-"))

    elif lvl ==  middle_line:
        print("WELCOME".center(widht,"-"))

    elif lvl > middle_line:
        items = max_draw - (((lvl-middle_line) - 1) * 2 )
        print(f'{items*pattern}'.center(widht,"-"))