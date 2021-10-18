from flask import Flask
app = Flask(__name__)

@app.route("/")
  
def hello():
    return bcolors.WARNING + "Aloha, Ohana!" + bcolors.ENDC
