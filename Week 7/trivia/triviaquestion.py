import random

class TriviaQuestion():

    NEXTQUESTIONID = 0

    def __init__(self,question,category,difficulty,answer,incAnswers):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.answer = answer
        self.incAnswers = incAnswers
        TriviaQuestion.NEXTQUESTIONID += 1
        self.id = TriviaQuestion.NEXTQUESTIONID
    
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
        shuffledAnswers = []
        shuffledAnswers.append(self.answer)
        for option in self.incAnswers:
            shuffledAnswers.append(option)
        random.shuffle(shuffledAnswers)
        return shuffledAnswers

    def getId(self):
        return int(self.id)