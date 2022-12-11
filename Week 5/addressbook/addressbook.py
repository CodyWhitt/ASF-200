class Contact():
    def __init__(self,firstName,lastName,emailAddress,phone,picLarge):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.phone = phone
        self.picLarge = picLarge

    # Getters
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def getEmailAddress(self):
        return self.emailAddress
 
    def getPhone(self):
        return self.phone

    def getPicLarge(self):
        return self.picLarge

    def __str__(self):
        retStr = "UserData: "
        retStr += (self.firstName) + ' '
        retStr += (self.lastName) + ' '
        retStr += (self.emailAddress) + ' '
        retStr += (self.phone) + ' '
        retStr += (self.picLarge) + ' '
        return retStr

    def __repr__(self):
        retRepr = "UserData: "
        retRepr += (self.firstName) + ' '
        retRepr += (self.lastName) + ' '
        retRepr += (self.emailAddress) + ' '
        retRepr += (self.phone) + ' '
        retRepr += (self.picLarge) + ' '
        return  retRepr
        
class AddressBook():
    def __init__(self):
        self.users = []

    def addUser(self, user):
        self.users.append(user)

    def showAllUsers(self):
        return self.users

    def findAllMatching(self, searchStr):
        results = []
        for user in self.users:
            if user.getFirstName().lower().startswith(searchStr.lower()) or user.getLastName().lower().startswith(searchStr.lower()):
                results.append(user)
                return results
        return None