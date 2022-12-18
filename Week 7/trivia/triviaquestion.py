class Contact():
    def __init__(self,question,category,difficulty,answer,incAnswers,id):
        self.question = question
        self.category = category
        self.difficulty = difficulty
        self.answer = answer
        self.incAnswers = incAnswers
        self.id = id
    
    # Getters
    def getQuestion(self):
        return self.question

    def getCategory(self):
        return self.category

    def getDifficulty(self):
        return self.difficulty

    def getAnswer(self):
        return self.answer

    def getIncAnswers(self):
        return self.incAnswers

    def getId(self):
        return self.id

    def getShuffledAnswers():
        # Create a method called "getShuffledAnswers" that returns a list containing the correct answer and the incorrect answers in a list that has been shuffled. 
        # Google "python shuffle list" for information on how to shuffle a list.  This class will be used to store a single trivia question.
        return None