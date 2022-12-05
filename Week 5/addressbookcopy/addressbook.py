import requests

class Contacts():
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

    def showAuthorizedUsers(self):
        for user in self.users:
            print(user)

    def searchForUser(self, firstName):
        for user in self.users:
            if (user.getUser() == firstName):
                return user
        return None
    
# Grabs data from provided API site
def getData():
    URL = "https://randomuser.me/api/?results=25"

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

# loop to store all requested data
users = AddressBook()
jsonUserData = getData()

for currentUser in jsonUserData["results"]:
    firstName = currentUser["name"]["first"]
    lastName = currentUser["name"]["last"]
    emailAddress = currentUser["email"]
    phone = currentUser["phone"]
    picLarge = currentUser["picture"]["large"]
    
    newUser = Contacts(firstName,lastName,emailAddress,phone,picLarge)
    users.addUser(newUser)