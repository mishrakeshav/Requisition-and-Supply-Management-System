from flask_wtf import FlaskForm
from wtforms import ( 
    StringField, PasswordField ,
    DateTimeField,
    IntegerField, SubmitField,
    TextAreaField
    )

# from wtforms.fields.html5  import DateField,TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min = 2,max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min = 2,max=50)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    confirm_password =PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Account')

class UpdatePassword(FlaskForm):
    prev_password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    confirm_password =PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Update Password')



class RequestForm(FlaskForm):
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])
    message = TextAreaField('Request Message', validators=[DataRequired(), Length(min = 0,max=100)])
    submit = SubmitField('Confirm Request')


class EditStocks(FlaskForm):
    stock_id = IntegerField('Stock Id', validators=[DataRequired()])
    avail = IntegerField('Qty', validators=[DataRequired()])
    quantity_req = IntegerField('Required Qty.', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Previous Password', validators = [DataRequired(), Length(min = 4,max=20)])
    submit = SubmitField('Update Profile')