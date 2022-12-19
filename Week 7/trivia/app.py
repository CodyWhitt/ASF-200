from flask import Flask, request, render_template
import requests
import triviaquestion
import triviagame

app = Flask(__name__)

def getData():
    URL = "https://opentdb.com/api.php?amount=5"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

questions = triviaquestion.QuestionLog()
jsonQuestionData = getData()

for currentQuestions in jsonQuestionData["results"]:
    question = currentQuestions["question"]
    category = currentQuestions["category"]
    difficulty = currentQuestions["difficulty"]
    answer = currentQuestions["correct_answer"]
    incAnswers = currentQuestions["incorrect_answers"]
    
    newQuestion = triviaquestion.TriviaQuestion(question,category,difficulty,answer,incAnswers)
    questions.addQuestion(newQuestion)

@app.route("/")
def home():
    return render_template('index.html',questions = questions.showAllQuestions())

# @app.route('/score', methods=['POST'])
# def checkAnswers():
#     if request.method == 'POST':
#         correctlyAnsweredQuestions = []
#         incorrectlyAnsweredQuestions = []
#         for question in gameBoardQuestions:
#             if (request.form[str(question.getID())] == question.getCorrectAnswer()):
#                 correctlyAnsweredQuestions.append(question)
#             else:
#                 incorrectlyAnsweredQuestions.append(question)        
                
#         # proccess user guesses to questions
#         return render_template(....)

if __name__ == "__main__":
    app.run()