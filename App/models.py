from App import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(250), unique = True , nullable = False)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    password = db.Column(db.String(60), nullable = False)
    isAdmin = db.Column(db.Boolean, default = False)
    

    def __repr__(self):
        return str({
            'email' : self.email,
            'name' : self.first_name + " " + self.last_name,
        })


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item = db.Column(db.String(255), nullable = False)
    qty_prev = db.Column(db.Integer, nullable = False)
    avail = db.Column(db.Integer, nullable = False)
    qty_req = db.Column(db.Integer, nullable = False)
    qty_pres = db.Column(db.Integer, default = 0)
    

class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    stock_id = db.Column(db.Integer,  nullable = False)
    qty = db.Column(db.Integer)
    date_applied = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    status = db.Column(db.Integer, default = 0)


