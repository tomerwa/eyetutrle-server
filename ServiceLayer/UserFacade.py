from DomainLayer.LogicRequests import *
from DomainLayer.Question import *

class UserFacade:

    def __init__(self):
        self.logic_requests = LogicRequests()

    def login(self, user_id):
        if not LogicRequests.valid_id(user_id):
            return 0
        user = self.logic_requests.get_user(user_id)
        if user is None:
            return 0
        elif user.is_admin():
            return 1
        else:
            return 2

    def start_test(self, number_of_questions=10):
        return self.logic_requests.generate_test(number_of_questions)

    def end_test(self, user_id, selected_answers):
        grade = self.logic_requests.calculate_grade(selected_answers)
        self.logic_requests.update_grade(user_id, grade)
        return grade

    def watch_grades(self, user_id):
        user = self.logic_requests.get_user(user_id)
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
        return self.logic_requests.add_question(question)

    def remove_question(self, question_id):
        return self.logic_requests.remove_question(question_id)







