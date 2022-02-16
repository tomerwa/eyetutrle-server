from flask import Flask, request
from ServiceLayer.UserFacade import *

app = Flask(__name__)
user_facade = UserFacade()


@app.route("/tts")
def tts():
    question_id = request.data['question_id']
    user_facade.tts(question_id)


@app.route("/login")
def login():
    user_id = request.data['user_id']
    return user_facade.login(user_id=user_id)


@app.route("end_test", methods=['POST'])
def end_test():
    user_id = request.json['user_id']
    selected_answers = request.json['selected_answers']
    return user_facade.end_test(user_id=user_id, selected_answers=selected_answers)


@app.route("/grades")
def get_grades():
    user_id = request.data['user_id']
    return user_facade.watch_grades(user_id=user_id)


@app.route("/question")
def add_question():
    limit = request.data['limit']
    if not limit:
        limit = 200
    return user_facade.start_test(limit)


@app.route("/question", methods=['POST'])
def add_question():
    content = request.json['content']
    possible_answers = request.json['possible_answers']
    correct_answer = request.json['correct_answer']
    return user_facade.add_question(content=content, possible_answers=possible_answers, correct_answer=correct_answer)


@app.route("/question", methods=['DELETE'])
def remove_question():
    question_id = request.data['question_id']
    return user_facade.remove_question(question_id)


if __name__ == '__main__':
    app.run()
