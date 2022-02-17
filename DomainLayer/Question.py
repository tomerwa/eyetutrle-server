import json


class Question:

    def __init__(self, id, content=None, possible_answers=None, correct_answer=None):
        self.id = id
        self.content = content
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer

    def add_possible_answer(self, possible_answer):
        self.possible_answers.append(possible_answer)

    def remove_possible_answer(self, possible_answer):
        self.possible_answers.remove(possible_answer)

    def toJSON(self):
        return {
            'id': self.id,
            'content': self.content,
            'possible_answers': self.possible_answers,
            'correct_answer': self.correct_answer
        }
