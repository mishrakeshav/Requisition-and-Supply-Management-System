from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import ( 
    StringField, PasswordField ,
    DateTimeField, DecimalField,
    IntegerField, SubmitField
                    )
from wtforms.fields.html5  import DateField,TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8,max=20)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min = 2,max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min = 2,max=50)])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 8,max=20)])
    confirm_password =PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class ExtendedHoursForm(FlaskForm):
    bill_date = DateField('Bill date',validators=[DataRequired()])
    from_time = TimeField('From Timing', validators=[DataRequired()])
    to_time = TimeField('To Timing', validators=[DataRequired()])
    bill_amount = DecimalField('Bill Amount', places = 2, validators=[DataRequired()])
    bill_image = FileField('Upload Bill', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

class LocalConveyanceForm(FlaskForm):
    from_location = StringField('From', validators = [DataRequired()])
    to_location = StringField('To', validators = [DataRequired()])
    kilometers = DecimalField('Kilometers', places = 2, validators=[DataRequired()])
    bill_date = DateField('Bill date',validators=[DataRequired()])
    bill_amount = DecimalField('Bill Amount', places = 2, validators=[DataRequired()])
    bill_image = FileField('Upload Bill', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')


class ClientEntertainmentForm(FlaskForm):
    client_name = StringField('Name of the client', validators = [DataRequired()])
    hotel_name = StringField('Name of the Hotel/Restaurant', validators = [DataRequired()])
    bill_date = DateField('Bill date',validators=[DataRequired()])
    bill_amount = DecimalField('Bill Amount', places = 2, validators=[DataRequired()])
    bill_image = FileField('Upload Bill', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

class OfficeExpensesForm(FlaskForm):
    bill_date = DateField('Bill date',validators=[DataRequired()])
    bill_no = IntegerField('Bill no', validators = [DataRequired()])
    bill_amount = DecimalField('Bill Amount', places = 2, validators=[DataRequired()])
    bill_image = FileField('Upload Bill', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')