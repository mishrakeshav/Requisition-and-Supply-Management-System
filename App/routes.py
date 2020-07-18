from flask import (
    render_template, url_for, flash, redirect, request, abort, send_file
)

from App.forms import (
    LoginForm, EditStocks, RequestForm, ProfileForm
)

from App.models import (
    User, Stock, Request
)
import csv, os


from App import app, db, bcrypt

from flask_login import login_user, current_user, logout_user, login_required





# ----------------- Admin routes ------------------
@app.route('/admin/requests')
@login_required
def admin_request():
    if not current_user.isAdmin: abort(403) 
    request = Request.query.all()[::-1]
    return render_template('request.html', requests = request) 


@app.route('/admin/stocks', methods = ['GET','POST'])
@login_required
def stocks():
    if not current_user.isAdmin: abort(403) 
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
    if not current_user.isAdmin: abort(403) 
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

@app.route('/admin/stock/download', methods = ['POST'])
@login_required
def download():
    if not current_user.isAdmin: abort(403) 
    stocks = Stock.query.all()
    path =os.path.join(app.root_path , 'static/downloads/stock.csv')
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Previous semester', 'Available', 'Quantity Required', 'Quantity present'])
        for element in stocks:
            writer.writerow([element.id, element.qty_prev, element.avail, element.qty_req, element.qty_pres])
    return send_file(path, as_attachment=True)



@app.route('/admin/stock/reset')
@login_required
def reset():
    if not current_user.isAdmin: abort(403) 
    stocks = Stock.query.all()
    path =os.path.join(app.root_path , 'static/downloads/stock.csv')
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Previous semester', 'Available', 'Quantity Required', 'Quantity present'])
        for element in stocks:
            writer.writerow([element.id, element.qty_prev, element.avail, element.qty_req, element.qty_pres])
    for element in stocks:
        element.qty_prev = element.qty_pres
        element.qty_pres = 0 
    return send_file(path, as_attachment=True)

     



@app.route('/admin/request/accept/<int:req_id>', methods = ['POST'])
@login_required
def accept_request(req_id):
    if not current_user.isAdmin: abort(403) 
    req  = Request.query.get_or_404(req_id)
    if req.qty > req.stock.avail:
        new_req = Request(user_id = req.user_id, stock_id = req.stock_id, qty = req.stock.avail, status = 1)
        db.session.add(new_req)
        req.qty = req.qty - req.stock.avail 
        req.stock.qty_pres +=  req.stock.avail
        req.stock.avail = 0
        
    else:
        req.stock.avail -= req.qty 
        req.stock.qty_pres += req.qty
        req.status = 1
    db.session.commit() 
    flash('Request Accepted','success')
    return redirect(url_for('admin_request'))


    


@app.route('/admin/request/delete/<int:req_id>', methods = ['POST'])
@login_required
def reject_request(req_id):
    if not current_user.isAdmin: abort(403) 
    req  = Request.query.get_or_404(req_id)
    req.status = -1
    db.session.commit()
    flash('Request rejected','success')
    return redirect(url_for('admin_request'))


@app.route('/admin/requests/summary')
@login_required
def admin_summary():
    if not current_user.isAdmin: abort(403) 
    requests = Request.query.all()[::-1]
    return render_template('summary.html', requests = requests)


# ----------------- User routes ------------------
@app.route('/')
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
            flash(f'Request Made Successfully', 'success')
        else:
            flash(f'Invalid Details')
    stocks = Stock.query.all()
    return render_template("user.html", stocks = stocks)


@app.route('/user/request/summary')
@login_required
def user_summary():
    requests = User.query.get(current_user.id).requests[::-1]
    return render_template('summary.html', requests = requests)

#---------------- General Routes --------------------
@app.route("/profile", methods=['POST', 'GET'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if not bcrypt.check_password_hash(current_user.password, form.prev_password.data): 
            flash(f'Incorrect Password', 'danger')
        else:
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.email = form.email.data
            current_user.password = bcrypt.generate_password_hash(form.new_password.data)
            db.session.commit()
            flash('Account was Updated', 'success')
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email

    return render_template('profile.html', form = form)

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
            return redirect(next_page) if next_page else  redirect(url_for('user_home'))
        else:
            flash(f"Your login credentials don't match", 'danger')
    
        
    return render_template('login.html',form = form)

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))