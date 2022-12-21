from flask import Flask, request, render_template

import triviaquestion
import triviagame

app = Flask(__name__)

newGame = triviagame.TriviaGame()
newGame.loadQuestions()
gameBoardQuestions = newGame.getAllQuestions()
print(gameBoardQuestions)

@app.route("/")
def home():
    return render_template('index.html',questions = newGame.getAllQuestions())

@app.route('/score', methods=['POST'])
def checkAnswers():
    if request.method == 'POST':
        correctlyAnsweredQuestions = []
        incorrectlyAnsweredQuestions = []
        for question in gameBoardQuestions:
            if (request.form[str(question.getID())] == question.getAnswer()):
                correctlyAnsweredQuestions.append(question)
            else:
                incorrectlyAnsweredQuestions.append(question)        
                
        # proccess user guesses to questions
        return render_template('scorecard.html')

if __name__ == "__main__":
    app.run()