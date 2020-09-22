from App import db, login_manager,app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


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
    isSuperUser = db.Column(db.Boolean, default = False)
    requests = db.relationship('Request', backref='user', lazy=True)
    special_requests = db.relationship('SpecialRequest', backref='user', lazy=True)
    # bills = db.relationship('Bill', backref='user', lazy=True)
    picture = db.Column(db.String(60), nullable=False, default='default.jpg')

    def get_reset_token(self,expires_sec = 1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return str({
            'email' : self.email,
            'name' : self.first_name + " " + self.last_name,
        })


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    picture = db.Column(db.String(60), nullable = False, default = 'default.jpg')
    stocks = db.relationship('Stock', backref='category', lazy=True)

    def __repr__(self):
        return str({
            'categoryName' : self.name,
        })


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable = False)
    item = db.Column(db.String(255), nullable = False)
    qty_prev = db.Column(db.Integer, nullable = False)
    avail = db.Column(db.Integer, nullable = False)
    qty_req = db.Column(db.Integer, nullable = False)
    qty_pres = db.Column(db.Integer, default = 0)
    minimum_limit = db.Column(db.Integer, nullable = False)
    maximum_limit = db.Column(db.Integer, nullable = False)
    quota = db.Column(db.Integer, nullable = False)
    requests = db.relationship('Request', backref='stock', lazy=True)
    special_requests = db.relationship('SpecialRequest', backref='stock', lazy=True)

    def __repr__(self):
        return str({
            'stock id ': self.id ,
            'item name' : self.item
        })


class Request(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable = False)
    original_quantity = db.Column(db.Integer, nullable = False)
    qty = db.Column(db.Integer, nullable = False)
    date_applied = db.Column(db.DateTime, nullable = False, default = datetime.now)
    status = db.Column(db.Integer, default = 0)
    accepted = db.Column(db.Boolean, default = False)
    admins_comment = db.Column(db.Text, nullable = False, default="No Comments")
    users_comment = db.Column(db.Text, nullable = False)
    received_comment = db.Column(db.Text, default = "No Comments")
    processed_by = db.Column(db.String(255), nullable = False, default = 'Not yet Processed')


# class Bill(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key = True)
#     bill_number = db.Column(db.Integer, nullable=False)
#     cost = db.Column(db.Integer, nullable = False)
#     was_updated_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
#     last_updated = db.Column(db.DateTime, nullable = False, default = datetime.now)
#     picture = db.Column(db.String(60), nullable=False)

class SpecialRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable = False)
    original_quantity = db.Column(db.Integer, nullable = False)
    qty = db.Column(db.Integer, nullable = False)
    date_applied = db.Column(db.DateTime, nullable = False, default = datetime.now)
    status = db.Column(db.Integer, default = 0)
    admins_comment = db.Column(db.Text, nullable = False, default="No Comments")
    users_comment = db.Column(db.Text, nullable = False)
    processed_by = db.Column(db.String(255), nullable = False, default = 'Not yet Processed')

