from flask_wtf import FlaskForm
from wtforms import ( 
    StringField, PasswordField ,
    DateTimeField,
    IntegerField, SubmitField)

# from wtforms.fields.html5  import DateField,TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    submit = SubmitField('Login')


class RequestForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])


class EditStocks(FlaskForm):
    stock_id = IntegerField('Stock Id', validators=[DataRequired()])
    avail = IntegerField('Qty', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    prev_password = PasswordField('Previous Password', validators = [DataRequired(), Length(min = 4,max=20)])
    new_password = PasswordField('New Password', validators = [DataRequired(), EqualTo('confirm_password'), Length(min = 4,max=20)])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), Length(min = 4,max=20)])
    submit = SubmitField('Update Profile')