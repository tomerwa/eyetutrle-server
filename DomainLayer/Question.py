class Questions:

    def __init__(self, id, content=None, possible_answers=(), correct_answer=None):
        self.id = id
        self.content = content
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer

    def add_possible_answer(self, possible_answer):
        self.possible_answers.append(possible_answer)

    def remove_possible_answer(self, possible_answer):
        self.possible_answers.remove(possible_answer)


