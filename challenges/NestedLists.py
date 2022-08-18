'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == '__main__':
    # We will load them as tuples
    students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]
    ]
    # Process list of tuples:
    students = sorted(students, key=lambda tup: tup[1])
    students = [st for st in students if st[1] != students[0][1]] # Delete all with worst grade
    # Print second grade students
    seconds = [st[0] for st in students if st[1] == students[0][1]]
    seconds.sort()
    for name in seconds:
        print(name)