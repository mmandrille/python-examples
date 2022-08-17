'''
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
    Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

def students_generator():
    for r in  ["Krishna 67 68 69","Arjun 70 98 63", "Malika 52 56 60"]:
        yield r

if __name__ == '__main__':
    # Load Data
    student_marks = {}
    for e in students_generator():
        name, *line = e.split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # Input name
    query_name = input("Insert Name of Student you want the Percentage: ")
    # Resolution:
    print(
        f'{sum(student_marks[query_name])/len(student_marks[query_name]):.2f}'
    )