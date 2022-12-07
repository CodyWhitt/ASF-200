from flask import Flask, request, render_template
import addressbook

for 

app = Flask(__name__)

@app.route("/")
def home():
   return render_template('index.html',users=users)
# @app.route("/search")

if __name__ == "__main__":
    app.run()

# python -m venv farmersmarket
# virtualenv farmersmarket
# source farmersmarket/Scripts/activate
# export FLASK_DEBUG=1