from flask import Flask, request, render_template
import addressBook
import requests

# Grabs data from provided API site
def getData():
    URL = "https://randomuser.me/api/?results=25&nat=us"

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
users = addressBook.AddressBook()
jsonUserData = getData()

for currentUser in jsonUserData["results"]:
    firstName = currentUser["name"]["first"]
    lastName = currentUser["name"]["last"]
    emailAddress = currentUser["email"]
    phone = currentUser["phone"]
    picLarge = currentUser["picture"]["large"]
    
    newUser = addressBook.Contact(firstName,lastName,emailAddress,phone,picLarge)
    users.addUser(newUser)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html',users=users.showAllUsers())

@app.route("/search/", methods=['POST'])
def search():
    search = request.form.get("search")
    return render_template('index.html',users=users.findAllMatching(search))

if __name__ == "__main__":
    app.run()

# python -m venv farmersmarket
# virtualenv farmersmarket
# source farmersmarket/Scripts/activate
# export FLASK_DEBUG=1