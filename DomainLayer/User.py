class User:

    def __init__(self, id, grades=None):
        self.id = id
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades
