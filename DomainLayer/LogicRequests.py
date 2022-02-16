import json
from Question import Questions

QUESTIONS = '..\\questions.json'

class LogicRequests:

    def __init__(self):
        self.user = None
        self.questions = LogicRequests.read_questions()

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
            questions.append(Questions(key, str(val['text']), list(val['answers']), int(val['correct'])))
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

    @staticmethod
    def valid_id(id):
        if len(id) != 9:
            return False
        return sum((int(digit) * (idx % 2 + 1)) % 10 + (int(digit) * (idx % 2 + 1)) / 10 for idx, digit in
                   enumerate(id)) % 10 == 0