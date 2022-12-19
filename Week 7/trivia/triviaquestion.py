import random

class TriviaQuestion():
    def __init__(self,question,category,difficulty,answer,incAnswers):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.answer = answer
        self.incAnswers = incAnswers

        # self.id = id
    
    # Getters
    def getQuestion(self):
        return str(self.question)

    def getCategory(self):
        return str(self.category)

    def getDifficulty(self):
        return str(self.difficulty)

    def getAnswer(self):
        return str(self.answer)

    def getIncAnswers(self):
        return [self.incAnswers]

    def getShuffledAnswers(self):
        self.shuffledAnswers = []
        self.shuffledAnswers.append(self.answer)
        for option in self.incAnswers:
            self.shuffledAnswers.append(option)
        random.shuffle(self.shuffledAnswers)
        return self.shuffledAnswers

    # def getId(self):
        # return int(self.id)

class QuestionLog():
    def __init__(self):
        self.questions = []
    
    def addQuestion(self, question):
        self.questions.append(question)

    def showAllQuestions(self):
        return self.questions
    
    def showAllAnswers(self):
        return 


    # def __str__(self):
    #     retStr = "UserData: "
    #     retStr += (self.question) + ' '
    #     retStr += (self.category) + ' '
    #     retStr += (self.difficulty) + ' '
    #     retStr += (self.answer) + ' '
    #     # retStr += (self.incAnswers) + ' '
    #     # retStr += (self.id) + ' '
    #     return retStr

    # def __repr__(self):
    #     retRepr = "UserData: "
    #     retRepr += (self.question) + ' '
    #     retRepr += (self.category) + ' '
    #     retRepr += (self.difficulty) + ' '
    #     retRepr += (self.answer) + ' '
    #     retRepr += (self.incAnswers) + ' '
    #     retRepr += (self.id) + ' '
    #     return  retRepr

    # class TriviaAnswers():
    #     def __init__(self):
    #         self.answers=[]
    #     def getShuffledAnswers(self):
    #         results = []
    #         for incAnswer in self.incAnswers:
    #             results.append(incAnswer)
    #             return results
    #         return None