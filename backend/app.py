# this is the main file containing all the routes and resources and also the instance 
# of the app server which however gets called in the 'runserver.py' file
from flask import Flask

app = Flask(__name__)

@app.route("/home")
def home():
    return "testing route..."