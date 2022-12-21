import requests
import triviaquestion

class TriviaGame():
    def __init__(self):
        self.questions = []
        self.answers = []
    
    def addQuestion(self, question):
        self.questions.append(question)

    def getAllQuestions(self):
        return self.questions

    def getData(self):
        URL = "https://opentdb.com/api.php?amount=5&category=18&difficulty=easy&type=multiple"

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

    def loadQuestions(self):

        jsonQuestionData = self.getData()

        for currentQuestions in jsonQuestionData["results"]:
            question = currentQuestions["question"]
            category = currentQuestions["category"]
            difficulty = currentQuestions["difficulty"]
            answer = currentQuestions["correct_answer"]
            incAnswers = currentQuestions["incorrect_answers"]
    
            newQuestion = triviaquestion.TriviaQuestion(question,category,difficulty,answer,incAnswers)
            self.addQuestion(newQuestion)
        
        
