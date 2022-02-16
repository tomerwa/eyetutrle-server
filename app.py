from flask import Flask, request
from ServiceLayer.UserFacade import *

app = Flask(__name__)
user_facade = UserFacade()


@app.route("/login")
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return 'Hello World!'

# get_questions -> {a: question, b: question, c: question}
# get_all_questions
# tts (full question)
@app.route("/login")
def login():
    user_id = request.data['user_id']
    return user_facade.login(user_id=user_id)


@app.route("end_test")
def end_test():
    user_id = request.data['user_id']
    selected_answers = request.data['selected_answers']
    return user_facade.end_test(user_id=user_id, selected_answers=selected_answers)


@app.route("/grades")
def get_grades():
    user_id = request.data['user_id']
    return user_facade.watch_grades(user_id=user_id)


@app.route("/questions")
def add_question():
    content = request.data['content']
    possible_answers = request.data['possible_answers']
    correct_answer = request.data['correct_answer']
    return user_facade.add_question(content=content, possible_answers=possible_answers, correct_answer=correct_answer)


@app.route("/questions")
def remove_question():
    question_id = request.data['question_id']
    return user_facade.remove_question(question_id)


@app.route()


if __name__ == '__main__':
    app.run()
