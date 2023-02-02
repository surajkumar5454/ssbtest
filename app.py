from datetime import datetime
from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import os
app = Flask(__name__)
app.secret_key = 'secret_key'  # Replace with a secret key of your own

UPLOAD_FOLDER = "papers"


@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        questions_file = request.files["questions_file"]

        # Save the questions file to the uploads folder
        filename = questions_file.filename
        questions_file.save(os.path.join(UPLOAD_FOLDER, filename))

        return redirect(url_for("index"))

    return render_template("admin.html")


def populate(test_type):

    excel_path = "papers"
    excel_filename = excel_path+"/"+test_type
    df = pd.read_excel(excel_filename)
    questions = []
    for i in range(len(df)):
        question = {}
        question["id"] = df.iloc[i]["id"]
        question["text"] = df.iloc[i]["text"]
        question["options"] = [df.iloc[i]["option1"], df.iloc[i]["option2"],
                               df.iloc[i]["option3"], df.iloc[i]["option4"]]
        question["answer"] = df.iloc[i]["answer"]
        questions.append(question)
    return questions


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    score = 0
    return render_template("result.html", score=score)


# def writetofile(score, total_correct, total_wrong, total_unanswered):
#     username = session.get("username")
#     test_type = session.get("test_type")
#     test_type = test_type.split('.')
#     current_datetime = datetime.now()
#     file = open(f"static/{username}-{test_type[0]}.txt", "a+")
#
#     # Write to the file
#     file.write(f"Name: {username}\nTest Type: {test_type[0]}\nTotal Correct: {total_correct}\nTotal Incorrect: {total_wrong}\nTotal Unanswered: {total_unanswered}\nFinal Score: {score}\nDate/Time: {current_datetime}")
#
#     # Close the file
#     file.close()


@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        username = request.args.get('username')
        test_type = request.args.get('questionpaper')
        session["username"] = username
        session["test_type"] = test_type
        questions = populate(test_type)
        return render_template("test.html", questions=questions)

    if request.method == "POST":
        score = 0
        total_unanswered = 0
        total_correct = 0
        total_wrong = 0
        test_type = session.get("test_type")
        questions = populate(test_type)
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
        score = total_correct - (total_wrong * 0.25)
        # writetofile(score, total_correct, total_wrong, total_unanswered)
        return render_template("result.html", score=score, questions=questions, total_questions=total_questions,
                               total_correct=total_correct, total_wrong=total_wrong, total_unanswered=total_unanswered)


if __name__ == "__main__":
    app.run(debug=True)
