class User:

    def __init__(self, id, username=None, password=None, grade=0):
        self.id = id
        self.username = username
        self.password = password
        self.grade = grade

    def calculate_grade(self, correct_answers, total_questions):
        self.grade = correct_answers // total_questions
