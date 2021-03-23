from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'
        #terminal% python3
        #>>> from flask_hello_app import Person
        #>>> print(Person.query.first())
        #<Person ID: 1, name: Sezin>
        #>>> Person.query.all()
        #[<Person ID: 1, name: Sezin>]

db.create_all() #table-called persons-is created 

@app.route('/')
def index():
    person = Person.query.first() #it takes the first element's name from table persons
    return 'Hello ' + person.name

#you can run this app by writing the command below to terminal
#FLASK_APP=flask-hello-app.py flask run

#For debug mode, you can run this app by writing the command below to terminal
#FLASK_APP=flask-hello-app.py FLASK_DEBUG=true flask run

#if you add the code which is below, you can run the app by writing the command: python flask-hello-app.py
if __name__ == '__main__':
  app.run()
