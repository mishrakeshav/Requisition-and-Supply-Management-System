from flask import (
    render_template, url_for, flash, redirect, request, abort
)

from ClaimSettlementApp.forms import (
    LoginForm, RegistrationForm, ExtendedHoursForm, 
    LocalConveyanceForm, OfficeExpensesForm, ClientEntertainmentForm
)

from ClaimSettlementApp.models import (
    User, ExtendedHoursClaim, ClientEntertainmentClaim, 
    LocalConveyanceClaim, OfficeExpensesClaim, Claims
)

import os
import secrets
from PIL import Image
import functools


from ClaimSettlementApp import app, db, bcrypt

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
def home():
    return redirect(url_for('login'))

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
@app.route("/claims")
@login_required
@only_admins
def claims():
    claims = Claims.query.all()[::-1]
    return render_template('claims_list.html', claims = claims)

@app.route("/claims/<string:type_of_claim>/<int:claim_id>/<int:claim>")
@login_required
def view_claim(type_of_claim,claim_id,claim):
    if current_user.isAdmin:
        if type_of_claim == "Extended Working Hours":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = ExtendedHoursClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Local Conveyance":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = LocalConveyanceClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Client Entertainment":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = ClientEntertainmentClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Office Expenses":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = OfficeExpensesClaim.query.filter_by(id = claim_id).first()
        return render_template('display_claim.html',user = user, mapped = mapped, clients_claim = clients_claim )
    else:
        return "URL NOT FOUND"

@app.route("/claims/<int:approved>/<string:type_of_claim>/<int:claim_id>/<int:claim>")
@login_required
def approve_claim(approved, type_of_claim, claim_id, claim):
    if current_user.isAdmin:
        if type_of_claim == "Extended Working Hours":
            mapped = Claims.query.filter_by(id = claim).first()
            mapped.approved = approved
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = ExtendedHoursClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Local Conveyance":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = LocalConveyanceClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Client Entertainment":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = ClientEntertainmentClaim.query.filter_by(id = claim_id).first()
        elif type_of_claim == "Office Expenses":
            mapped = Claims.query.filter_by(id = claim).first()
            user = User.query.filter_by(id = mapped.user_id).first()
            clients_claim = OfficeExpensesClaim.query.filter_by(id = claim_id).first()
        mapped.approved = approved
        db.session.commit()
        return redirect(url_for('claims'))
    else:
        return "URL NOT FOUND"

#######################################################################
#################### END POINTS FOR USER ##############################
#######################################################################
@app.route("/claims/apply/extended-working-hours", methods = ['GET', 'POST'])
@login_required
def extendedWorkingHours():
    form = ExtendedHoursForm()
    if form.validate_on_submit():
        bill_image = save_picture(form.bill_image.data)
        claim = ExtendedHoursClaim(
            from_time = str(form.from_time.data), 
            to_time = str(form.to_time.data),
            bill_amount = float(form.bill_amount.data),
            bill_date = form.bill_date.data,
            bill_image = bill_image
        )
        db.session.add(claim)
        db.session.commit()
        mapping_claim = Claims(
            claim_type = "Extended Working Hours",
            claim_id = claim.id ,
            user_id = current_user.id,
        )
        db.session.add(mapping_claim)
        db.session.commit()
        flash(f"Your claim has been made!", 'success')
        return redirect(url_for('client_history'))
    return render_template('extended_working_hours.html', form = form)

@app.route("/claims/apply/local-conveyance", methods = ['GET', 'POST'])
@login_required
def localConveyance():
    form = LocalConveyanceForm()
    
    if form.validate_on_submit():
        bill_image = save_picture(form.bill_image.data)
        claim = LocalConveyanceClaim(
            from_location = form.from_location.data,
            to_location = form.to_location.data,
            bill_amount = float(form.bill_amount.data),
            bill_date = form.bill_date.data,
            bill_image = bill_image
        )
        db.session.add(claim)
        db.session.commit()
        mapping_claim = Claims(
            claim_type = "Local Conveyance",
            claim_id = claim.id ,
            user_id = current_user.id,
        )
        db.session.add(mapping_claim)
        db.session.commit()
        flash(f"Your claim has been made!", 'success')
        return redirect(url_for('client_history'))
    return render_template('local_conveyance.html', form = form)

@app.route("/claims/apply/client-entertainment", methods = ['GET', 'POST'])
@login_required
def clientEntertainment():
    form = ClientEntertainmentForm()
    if form.validate_on_submit():
        bill_image = save_picture(form.bill_image.data)
        claim = ClientEntertainmentClaim(
            client_name = form.client_name.data,
            hotel_name = form.hotel_name.data,
            bill_amount = float(form.bill_amount.data),
            bill_date = form.bill_date.data,
            bill_image = bill_image
        )
        db.session.add(claim)
        db.session.commit()
        mapping_claim = Claims(
            claim_type = "Client Entertainment",
            claim_id = claim.id ,
            user_id = current_user.id,
        )
        db.session.add(mapping_claim)
        db.session.commit()
        flash(f"Your claim has been made!", 'success')
        return redirect(url_for('client_history'))
    return render_template('client_entertainment.html', form = form)

@app.route("/claims/apply/office-expenses", methods = ['GET', 'POST'])
@login_required
def officeExpenses():
    form = OfficeExpensesForm()
    if form.validate_on_submit():
        bill_image = save_picture(form.bill_image.data)
        claim = OfficeExpensesClaim(
            bill_no = form.bill_no.data,
            bill_amount = float(form.bill_amount.data),
            bill_date = form.bill_date.data,
            bill_image = bill_image
        )
        db.session.add(claim)
        db.session.commit()
        mapping_claim = Claims(
            claim_type = "Office Expenses",
            claim_id = claim.id,
            user_id = current_user.id,
        )
        db.session.add(mapping_claim)
        db.session.commit()
        flash(f"Your claim has been made!", 'success')
        return redirect(url_for('client_history'))
    return render_template('office_expenses.html', form = form)

@app.route("/claims/history")
@login_required
def client_history():
    history = Claims.query.filter_by(user_id = current_user.id)
    return render_template('history.html', history = history)

@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html')

#####################################################################