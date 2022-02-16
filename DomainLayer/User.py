class User:

    def __init__(self, id, grades=None):
        self.id = id
        self.grades = grades

    def calculate_grade(self, correct_answers, total_questions):
        self.grades.append(correct_answers // total_questions)

    def get_grades(self):
        return self.grades
