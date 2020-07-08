from ClaimSettlementApp import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(20), unique = True , nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(60), nullable = False)
    isAdmin = db.Column(db.Boolean, default = False)
    claims_made  = db.relationship('Claims', backref = 'claims', lazy = True)
    

    def __repr__(self):
        return str({
            'email' : self.email,
            'name' : self.first_name + " " + self.last_name,
        })



class Claims(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    claim_type = db.Column(db.String)
    claim_id = db.Column(db.Integer) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    approved = db.Column(db.Integer, default = 0)
    date_applied = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return str({
            'email' : self.user_id.email,
            'Claim Type' : self.claim_type,
            'user_id' : self.user_id,
            'approved' : self.approved,
            'date_applied' : self.date_applied
        })


class ExtendedHoursClaim(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    from_time = db.Column(db.String, nullable = False)
    to_time = db.Column(db.String, nullable = False) 
    bill_amount = db.Column(db.Float, nullable = False) 
    bill_date = db.Column(db.DateTime, nullable = False)
    bill_image = db.Column(db.String)

class ClientEntertainmentClaim(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    client_name = db.Column(db.String, nullable = False)
    hotel_name = db.Column(db.String, nullable = False)
    bill_amount = db.Column(db.Float, nullable = False) 
    bill_date = db.Column(db.DateTime, nullable = False)
    bill_image = db.Column(db.String)


class LocalConveyanceClaim(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    from_location = db.Column(db.String, nullable = False)
    to_location = db.Column(db.String, nullable = False) 
    bill_amount = db.Column(db.Float, nullable = False) 
    bill_date = db.Column(db.DateTime, nullable = False)
    bill_image = db.Column(db.String)

class OfficeExpensesClaim(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bill_no = db.Column(db.Integer, nullable = False)
    bill_amount = db.Column(db.Float, nullable = False) 
    bill_date = db.Column(db.DateTime)
    bill_image = db.Column(db.String)

