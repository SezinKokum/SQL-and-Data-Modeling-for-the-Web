from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

#you can run this app by writing the command below to terminal
#FLASK_APP=flask-hello-app.py flask run