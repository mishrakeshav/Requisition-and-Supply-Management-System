from flask import (
    render_template, url_for, flash, redirect, request, abort
)

from App.forms import (
    LoginForm, RegistrationForm
)

from App.models import (
    User, Stock, Request
)

import os
import secrets
from PIL import Image
import functools


from App import app, db, bcrypt

from flask_login import login_user, current_user, logout_user, login_required



###################### Utils ###########################


def only_admins(func):
    @functools.wraps(func)
    def function_that_runs_func():
        if current_user.isAdmin:
            return func()
        else:
            return "URL not found"
    return function_that_runs_func

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path , 'static/bills' , picture_fn)
    print(picture_path)

    
    i = Image.open(form_picture)
    
    i.save(picture_path)
    
    return picture_fn
###########################################################

@app.route("/")
@login_required
def home():
    return "Your are at your home"

@app.route("/login",methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('extendedWorkingHours'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get('next')
            login_user(user)
            flash('Your are now logged in', 'success')
            return redirect(next_page) if next_page else  redirect(url_for('extendedWorkingHours'))
        else:
            flash(f"Your login credentials don't match")
        
    return render_template('login.html',form = form)


@app.route("/register",methods = ['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('claims'))
    form = RegistrationForm()
    if form.validate_on_submit():
        password = bcrypt.generate_password_hash(form.password.data)
        user = User(
            email = form.email.data,
            password = password, 
            first_name = form.first_name.data,
            last_name = form.last_name.data
         )
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to log in","success")
        return redirect(url_for('login'))
    return render_template('register.html',form = form)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))



##################################################################
################### END POINTS FOR ADMIN #########################
##################################################################




#######################################################################
#################### END POINTS FOR USER ##############################
#######################################################################


#####################################################################