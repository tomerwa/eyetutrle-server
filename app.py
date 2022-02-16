from flask import Flask, request
from ServiceLayer.UserFacade import *

app = Flask(__name__)
user_facade = UserFacade()


@app.route("/login")
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return 'Hello World!'

# login -> 0, 1, 2
# get_questions -> {a: question, b: question, c: question}
# get_all_questions
# tts (full question)
# end_test -> grade
# add_question
# remove_question


@app.route("/grades")
def get_grades():
    user_id = request.data['userId']
    return user_facade.watch_grades(user_id=user_id)


if __name__ == '__main__':
    app.run()
