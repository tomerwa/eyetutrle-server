from DomainLayer.LogicRequests import *
from DomainLayer.Question import *

class UserFacade:

    def __init__(self):
        self.logic_requests = LogicRequests()

    def login(self, id):
        if not self.logic_requests.valid_id(id):
            return None
        user = self.logic_requests.get_user(id)
        if user is None:
            return 0
        elif user.is_admin():
            return 1
        else:
            return 2

    def start_test(self, id, number_of_questions):
        user = self.logic_requests.get_user(id)
        test = self.logic_requests.generate_test(number_of_questions)
        return test

    def end_test(self, id, selected_answers):
        if len(selected_answers) != len(self.logic_requests.get_test()):
            return None
        user = self.logic_requests.get_user(id)
        grade = self.logic_requests.calculate_grade(selected_answers)
        user.update_grade(grade)
        return grade

    def watch_grades(self, id):
        user = self.logic_requests.get_user(id)
        if user is None:
            return None
        return user.get_grades()

    def add_question(self, content, possible_answers, correct_answer):
        if content is None or content == "":
            return False
        if possible_answers != 3:
            return False
        for answer in possible_answers:
            if answer is None or answer == "":
                return False
        if correct_answer < 0 or correct_answer > 2:
            return False
        question_id = self.logic_requests.generate_question_id()
        question = Question(question_id, content=content, possible_answers=possible_answers, correct_answer=correct_answer)
        self.logic_requests.add_question(question)
        return True

    def remove_question(self, question_id):
        question = self.logic_requests.get_question(question_id)
        self.logic_requests.remove_question(question)
        return True







