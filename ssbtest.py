from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


def populate():
    df = pd.read_excel("mcq.xlsx")
    questions = []
    for i in range(len(df)):
        question = {}
        question["id"] = df.iloc[i]["id"]
        question["text"] = df.iloc[i]["text"]
        question["options"] = [df.iloc[i]["option1"], df.iloc[i]["option2"],
                               df.iloc[i]["option3"], df.iloc[i]["option4"]]
        question["answer"] = df.iloc[i]["answer"]
        questions.append(question)
    print(len(questions))
    return questions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    score = 0
    return render_template("result.html", score=score)


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        questions = populate()
        print(questions)
        return render_template("test.html", questions=questions)

    if request.method == "POST":
        score = 0
        total_unanswered = 0
        total_correct = 0
        total_wrong = 0
        questions = populate()
        for question in questions:
            if str(question["id"]) in request.form:
                if request.form[str(question["id"])] == str(question["answer"]):
                    total_correct += 1
                    question["selected_answer"] = int(request.form[str(question["id"])])
                else:
                    question["selected_answer"] = int(request.form[str(question["id"])])
                    total_wrong += 1
            else:
                question["selected_answer"] = None
                total_unanswered += 1
        total_questions = len(questions)
        score = total_correct - (total_wrong*0.25)
        return render_template("result.html", score=score, questions=questions, total_questions=total_questions,
                               total_correct=total_correct, total_wrong=total_wrong, total_unanswered=total_unanswered)


if __name__ == "__main__":
    app.run(debug=True)
