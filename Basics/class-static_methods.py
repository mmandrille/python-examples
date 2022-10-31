# static.py
class ClassGrades:
    def __init__(self, grades):
        self.grades = grades

    @classmethod  # This method has access to the class
    def from_csv(cls, grade_csv_str):
        grades = map(int, grade_csv_str.split(', '))
        cls.validate(grades)  # We use the class static method here
        return cls(grades)

    @staticmethod  # This function dont has access to the class
    def validate(grades):
        for g in grades:
            if g < 0 or g > 100:
                raise Exception()


# Run our code
if __name__ == "__main__":
    try:
        # Try out some valid grades
        class_grades_valid = ClassGrades.from_csv('90, 80, 85, 94, 70')
        print(f'Got grades: {class_grades_valid.grades}')

        # Should fail with invalid grades
        class_grades_invalid = ClassGrades.from_csv('92, -15, 99, 101, 77, 65, 100')
        print(class_grades_invalid.grades)

    except Exception:
        print('Invalid!')
