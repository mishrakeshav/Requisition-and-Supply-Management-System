from flask_wtf import FlaskForm
from wtforms import ( 
    StringField, PasswordField ,
    DateTimeField,
    IntegerField, SubmitField,
    TextAreaField,
    SelectField,
    )

from flask_wtf.file import FileField, FileAllowed

# from wtforms.fields.html5  import DateField,TimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from App.models import User




class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4,max=20)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),  Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min = 2,max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min = 2,max=50)])
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
    stock_name = StringField('Stock Name', validators=[DataRequired()])
    avail = IntegerField('Quantity', validators=[DataRequired()])
    quantity_req = IntegerField('Required Quantity.', validators=[DataRequired()])
    category = SelectField('Category', coerce=int)
    maximum_limit = IntegerField('Maximum Limit', validators=[DataRequired()])
    minimum_limit = IntegerField('Minimum Limit', validators=[DataRequired()])
    quota = IntegerField('Quota', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Previous Password', validators = [DataRequired(), Length(min = 4,max=20)])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Profile')

class EditCategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    picture = FileField('Update Category Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Category')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
        validators = [DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email!')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])

    confirm_password = PasswordField('Confirm Password', 
        validators = [DataRequired(), EqualTo('password')])
        
    submit = SubmitField('Reset Password')