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



@app.route('/')
def home():
    pass


# ----------------- Admin routes ------------------
@app.route('/admin/requests')
def admin_request():
    pass

@app.route('/admin/stocks')
def stocks():
    pass


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