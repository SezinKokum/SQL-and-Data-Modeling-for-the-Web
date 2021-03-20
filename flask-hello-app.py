from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/mydb'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World!'

#you can run this app by writing the command below to terminal
#FLASK_APP=flask-hello-app.py flask run

#For debug mode, you can run this app by writing the command below to terminal
#FLASK_APP=flask-hello-app.py FLASK_DEBUG=true flask run

#if you add the code which is below, you can run the app by writing the command: python flask-hello-app.py
if __name__ == '__main__':
  app.run()