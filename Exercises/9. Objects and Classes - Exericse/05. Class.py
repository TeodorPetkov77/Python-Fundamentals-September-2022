class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade

    def __repr__(self):
        return f"The students in {self.name}: " \
               f"{', '.join(self.students)}. " \
               f"Average grade: {self.get_average_grade():.2f}"


