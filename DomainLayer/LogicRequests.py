import json
from Question import Question

QUESTIONS = '..\\questions.json'

class LogicRequests:

    def __init__(self):
        self.users = LogicRequests.read_users()
        self.questions = LogicRequests.read_questions()

    def get_user():
        pass

    def add_question(self, question: Question):
        self.questions.append(question)
        LogicRequests.write_questions(self.questions)

    def remove_question(self, question_id: str):
        del self.questions[question_id]
        LogicRequests.write_questions(self.questions)

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
        for key,val in data.items():
            questions.append(Question(key, str(val['text']), list(val['answers']), int(val['correct'])))
        return questions
    
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


    def valid_id(self, id):
        if len(id) != 9:
            return False
        return sum((int(digit) * (idx % 2 + 1)) % 10 + (int(digit) * (idx % 2 + 1)) / 10 for idx, digit in
                   enumerate(id)) % 10 == 0