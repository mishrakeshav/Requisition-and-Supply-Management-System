from flask import (
    render_template, url_for, flash, redirect, request, abort
)

from App.forms import (
    LoginForm, EditStocks, RequestForm, Profile, NewItemForm
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



@app.route('/')
def home():
    pass


# ----------------- Admin routes ------------------
@app.route('/admin/requests')
def admin_request():
    request = [
        
    ]
    return render_template('request.html', requests = request) 


@app.route('/admin/stocks', methods = ['GET','POST'])
def stocks():
    if request.method == 'GET':
        stocks = Stock.query.all()
        return render_template('stocks.html', stocks = stocks)
    else:
        stock = Stock.query.filter_by(id = request.form['id']).first()
        stock.avail = int(request.form['avail_text'] )
        stock.qty_req  = int(request.form['qty_text'] )
        db.session.commit()
        flash(f'Stock Updated', 'success')
        return redirect(url_for('stocks'))

        


@app.route('/admin/stocks/edit')
def edit_stocks():
    pass


@app.route('/admin/stocks/add')
def add_stocks():
    pass

@app.route('/admin/request/accept')
def accept_request():
    pass


@app.route('/admin/request/delete')
def reject_request():
    pass

@app.route('/admin/requests/summary')
def admin_summary():
    pass


# ----------------- User routes ------------------
@app.route('/user/home')
def user_home():
    pass

@app.route('/user/request/summary')
def user_summary():
    pass

#---------------- General Routes --------------------

@app.route("/login",methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            next_page = request.args.get('next')
            login_user(user)
            flash('Your are now logged in', 'success')
            return redirect(next_page) if next_page else  redirect(url_for('home'))
        else:
            flash(f"Your login credentials don't match")
        
    return render_template('login.html',form = form)

@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))