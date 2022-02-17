import json
import random
from DomainLayer.Question import *
from DomainLayer.User import *


QUESTIONS = 'questions.json'
USERS = 'users.json'

class LogicRequests:

    def __init__(self):
        self.users = LogicRequests.read_users()
        self.questions = LogicRequests.read_questions()

    def get_user(self, user_id):
        for usr in self.users:
            if usr.id == user_id:
                return usr
        return None

    def add_question(self, question: Question):
        self.questions.append(question)
        LogicRequests.write_questions(self.questions)
        return True

    def remove_question(self, question_id: str):
        del self.questions[int(question_id)]
        LogicRequests.write_questions(self.questions)
        return True

    @staticmethod
    def read_from_json(path: str):
        data = dict()
        with open(path, encoding='utf8') as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def write_to_json(path: str, data: dict):
        with open(path, 'w', encoding='utf8') as f:
            json.dump(data, f)

    @staticmethod
    def read_questions():
        questions = list()
        data = LogicRequests.read_from_json(QUESTIONS)
        for key, val in data.items():
            questions.append(Question(key, str(val['text']), list(val['answers']), int(val['correct'])))
        return questions

    @staticmethod
    def read_users():
        users = list()
        data = LogicRequests.read_from_json(USERS)
        for key, val in data.items():
            users.append(User(key, val))
        return users
    
    @staticmethod
    def write_questions(questions: list):
        data = dict()
        for q in questions:
            data[q.id] = {
                'text': q.content,
                'answers': q.possible_answers,
                'correct': q.correct_answer
            }
        LogicRequests.write_to_json(QUESTIONS, data)

    @staticmethod
    def write_users(users: list):
        data = dict()
        for u in users:
            data[u.id] = {
                'grades': u.grades
            }
        LogicRequests.write_to_json(USERS, data)

    @staticmethod
    def valid_id(user_id):
        if len(user_id) != 9:
            return False
        return True

    def calculate_grade(self, selected_answers):
        grade = 0
        for ans in selected_answers:
            if self.questions[int(ans.get('id'))].correct_answer == ans.get('answer'):
                grade += 1
        return grade * 100 / len(selected_answers)

    def generate_test(self, number_of_questions):
        lst = random.sample(self.questions, min(len(self.questions), int(number_of_questions)))
        res = list()
        for qst in lst:
            res.append(qst.toJSON())
        return res

    def generate_question_id(self):
        return len(self.questions)

    def update_grade(self, user_id, grade):
        self.get_user(user_id).add_grade(grade)
