from flask_wtf import FlaskForm
from wtforms import ( 
    StringField, PasswordField ,
    DateTimeField,
    IntegerField, SubmitField)

# from wtforms.fields.html5  import DateField,TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8,max=20)])
    submit = SubmitField('Login')

class NewItemForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])
    avail = IntegerField('Qty', validators=[DataRequired()])


class RequestForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])


class EditStocks(FlaskForm):
    avail = IntegerField('Qty', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])

class Profile(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New Password', validators = [DataRequired(), Length(min = 8,max=20)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), Length(min = 8,max=20)])
    