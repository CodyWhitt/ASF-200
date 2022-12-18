class TriviaQuestion():
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
        results = []
        for 

    def __str__(self):
        retStr = "UserData: "
        retStr += (self.question) + ' '
        retStr += (self.category) + ' '
        retStr += (self.difficulty) + ' '
        retStr += (self.answer) + ' '
        retStr += (self.incAnswers) + ' '
        retStr += (self.id) + ' '
        return retStr

    def __repr__(self):
        retRepr = "UserData: "
        retRepr += (self.question) + ' '
        retRepr += (self.category) + ' '
        retRepr += (self.difficulty) + ' '
        retRepr += (self.answer) + ' '
        retRepr += (self.incAnswers) + ' '
        retRepr += (self.id) + ' '
        return  retRepr
    
    class AddressBook():
    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)