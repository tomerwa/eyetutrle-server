from flask import Flask

app = Flask(__name__)


@app.route("/login")
@app.route("/", methods=["GET", "POST"])
def hello_world():
    return 'Hello World!'

# login -> 0, 1, 2
# get_questions -> {a: question, b: question, c: question}
# get_all_questions
# tts (full question)
# end_test -> grade
# get_grades
# add_question
# remove_question

if __name__ == '__main__':
    app.run()
