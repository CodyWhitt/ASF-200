import requests

# class for setters and getters for Users
class User():
    def __init__(self,firstName,lastName,emailAddress,userName,password,UUID,phone,cell,picLarge,picThumb):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.userName = userName
        self.password = password
        self.UUID = UUID
        self.phone = phone
        self.cell = cell
        self.picLarge = picLarge
        self.picThumb = picThumb
    
    # Setters
    def setFirstName(self, firstName):
        self.firstName = firstName
    
    def setLastName(self, lastName):
        self.lastName = lastName

    def setEmailAddress(self, emailAddress):
        self.emailAddress = emailAddress
    
    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password
    
    def setUUID(self, UUID):
        self.UUID = UUID

    def setPhone(self, phone):
        self.phone = phone
    
    def setCell(self, cell):
        self.cell = cell
    
    def setPicLarge(self, picLarge):
        self.picLarge = picLarge
    
    def setPicThumb(self, picThumb):
        self.picThumb = picThumb

    # Getters
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName

    def getEmailAddress(self):
        return self.emailAddress
    
    def getUserName(self):
        return self.userName

    def getPassword(self):
        return self.password
    
    def getUUID(self):
        return self.UUID

    def getPhone(self):
        return self.phone
    
    def getCell(self):
        return self.cell
    
    def getPicLarge(self):
        return self.picLarge
    
    def getPicThumb(self):
        return self.picThumb

    def __str__(self):
        retStr = "UserData: "
        retStr += (self.firstName) + ' '
        retStr += (self.lastName) + ' '
        retStr += (self.emailAddress) + ' '
        # retStr += (self.userName) + ' '
        # retStr += (self.password) + ' '
        # retStr += (self.UUID) + ' '
        # retStr += (self.phone) + ' '
        # retStr += (self.cell) + ' '
        # retStr += (self.picLarge) + ' '
        # retStr += (self.picThumb) + ' '
        return retStr

# 
class AuthorizedUsers():
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
    URL = "https://randomuser.me/api/?results=10"

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


users = AuthorizedUsers()
jsonUserData = getData()

# loop to store all requested data
for currentUser in jsonUserData["results"]:
    firstName = currentUser["name"]["first"]
    lastName = currentUser["name"]["last"]
    emailAddress = currentUser["email"]
    userName = currentUser["login"]["username"]
    password = currentUser["login"]["password"]
    UUID = currentUser["login"]["uuid"]
    phone = currentUser["phone"]
    cell = currentUser["cell"]
    picLarge = currentUser["picture"]["large"]
    picThumb = currentUser["picture"]["thumbnail"]
    
    newUser = User(firstName,lastName,emailAddress,userName,password,UUID,phone,cell,picLarge,picThumb)
    users.addUser(newUser)

# return requested data to terminal
users.showAuthorizedUsers()