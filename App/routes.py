from flask import (
    render_template, url_for, flash, redirect, request, abort
)

from App.forms import (
    LoginForm, EditStocks, RequestForm, Profile
)

from App.models import (
    User, Stock, Request
)



from App import app, db, bcrypt

from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
@login_required
def home():
    pass


# ----------------- Admin routes ------------------
@app.route('/admin/requests')
@login_required
def admin_request():
    request = [
        
    ]
    return render_template('request.html', requests = request) 


@app.route('/admin/stocks', methods = ['GET','POST'])
@login_required
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





@app.route('/admin/stocks/add', methods=['POST'])
@login_required
def add_stocks():
    err_flag = False
    form = request.form
    if form['qty_req'].isnumeric() and form['qty'].isnumeric():
        stck = Stock(
            item = form['item_name'],
            qty_prev = 0,
            avail = int(form['qty']),
            qty_req = int(form['qty_req']),
            qty_pres = 0
        )
        db.session.add(stck)
        db.session.commit()
        flash(f'Stock added Successfully', 'success')
    else:
        flash(f'Invalid Details', 'danger')

    return redirect(url_for('stocks'))


@app.route('/admin/request/accept')
@login_required
def accept_request():
    pass


@app.route('/admin/request/delete')
@login_required
def reject_request():
    pass

@app.route('/admin/requests/summary')
@login_required
def admin_summary():
    pass


# ----------------- User routes ------------------
@app.route('/user/home', methods=['GET', 'POST'])
@login_required
def user_home():
    if request.method == 'POST':
        form = request.form
        if form['id'].isnumeric() and form['qty'].isnumeric():
            stock = Stock.query.get_or_404(int(form['id']))
            req = Request(
                user_id = current_user.id,
                stock_id = int(form['id']),
                qty = int(form['qty'])
            )
            db.session.add(req)
            db.session.commit()
        else:
            flash(f'Invalid Details')
    stocks = Stock.query.all()
    return render_template("user.html", stocks = stocks)


@app.route('/user/request/summary')
@login_required
def user_summary():
    requests = Request.query\
        .join(Stock, Request.stock_id == Stock.id, Request.user_id == current_user.id)\
        
    return render_template('summary.html', requests = requests)

#---------------- General Routes --------------------

@app.route("/login",methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("here 1")
            next_page = request.args.get('next')
            login_user(user)
            print('here2')
            flash('Your are now logged in', 'success')
            return redirect(next_page) if next_page else  redirect(url_for('admin_request'))
        else:
            flash(f"Your login credentials don't match")
    
        
    return render_template('login.html',form = form)

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))