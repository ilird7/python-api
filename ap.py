
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/alchemy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    surname = db.Column(db.String(30), unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            "username": self.username
        }


class Customer(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(30), unique=True, nullable=False)
    surname = db.Column(db.String(30), unique=True, nullable=False)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "surname": self.surname
        }



@app.route('/emp')
def getEmps():
    emps = Employee.query.all()
    emp_list = []

    for emp in emps:
        emp_list.append(emp.serialize)
    return jsonify(emp_list)


@app.route('/costumers')
def getCostumers():
    costumers = Customer.query.all()
    cs_list = []

    for cs in costumers:
        cs_list.append(cs.serialize)
    return jsonify(cs_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3555, debug=True)

