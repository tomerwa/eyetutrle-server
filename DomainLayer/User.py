

class User:

    def __init__(self, id, is_admin=False, grades=None):
        self.id = id
        self.is_admin = is_admin
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def is_admin(self):
        return self.is_admin()

    def get_grades(self):
        return self.grades
