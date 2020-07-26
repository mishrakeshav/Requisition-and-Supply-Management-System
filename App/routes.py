from flask import (
    render_template, url_for, flash, redirect, request, abort, send_file
)

from App.forms import (
    LoginForm, EditStocks, RequestForm, ProfileForm, RegistrationForm,
    UpdatePassword
)

from App.models import (
    User, Stock, Request, Category
)
import csv
import os
import secrets
from PIL import Image
import functools



from App import app, db, bcrypt

from flask_login import login_user, current_user, logout_user, login_required





# ----------------- Admin routes ------------------

### Admin Stock Routes ###
@app.route('/admin/stocks', methods = ['GET','POST'])
@login_required
def stocks():
    if not current_user.isAdmin: abort(403) 
    categories = Category.query.all()
    if request.method == 'GET':
        stocks = Stock.query.all()
        return render_template('stocks.html', stocks = stocks, categories = categories)
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
    form = request.form
    if form['qty_req'].isnumeric() and form['avail'].isnumeric() \
        and form['quota'].isnumeric() and form['minimum_limit'].isnumeric()\
        and form['maximum_limit'].isnumeric():
        stck = Stock(
            item = form['name'],
            category_id = int(form['category_id']),
            qty_prev = 0,
            avail = int(form['avail']),
            qty_req = int(form['qty_req']),
            qty_pres = 0,
            maximum_limit = int(form['maximum_limit']),
            minimum_limit = int(form['minimum_limit']),
            quota = int(form['quota'])
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


### Admin Categories ###

# view all the categories
@app.route('/admin/categories')
def admin_categories():
    cat = Category.query.all()
    return render_template('admin_categories.html', categories = cat)

# view all the stocks in a category
@app.route('/admin/categories/<int:category_id>')
def admin_category(category_id):
    stocks = Stock.query.filter_by(category_id = category_id).all()
    quota = []
    for stock in stocks:
        requests = Request.query.filter_by(user_id = current_user.id, stock_id= stock.id).all()
        temp = 0
        for i in requests:
            if i.status == 0 or i.status == 1:
                temp += i.qty
        quota_left = max(0, stock.quota - temp)
        quota.append(quota_left)
    return render_template('user.html', stocks= stocks, quota = quota, length = len(quota))

# add a new category
@app.route('/admin/category/add', methods=['POST'])
@login_required
def add_category():
    if not current_user.isAdmin: abort(403) 
    form = request.form
    cat = Category(
        name=form['name'],
        picture = save_picture(request.files['picture'], 'category')
    )
    db.session.add(cat)
    db.session.commit()
    flash(f'Category added Successfully', 'success')

    return redirect(url_for('admin_categories'))


###Admin Request Routes  ###

#display all requests
@app.route('/admin/requests')
@login_required
def admin_request():
    if not current_user.isAdmin: abort(403) 
    request = Request.query.all()[::-1]
    return render_template('request.html', requests = request) 

#accept request
@app.route('/admin/request/accept/<int:req_id>', methods = ['POST'])
@login_required
def accept_request(req_id):    
    if not current_user.isAdmin : abort(403)
    request_quantity = request.form['request_quantity']
    admin_comment = request.form['admincomment']

    if not request_quantity.isnumeric():
        flash('Quantity should be a number', 'danger')
        return redirect(url_for('admin_request'))

    req  = Request.query.get_or_404(req_id)
    request_quantity = int(request_quantity)

    if request_quantity > req.original_quantity and request_quantity > req.stock.avail:
        flash('You cannot accept more than the user has requested or more than the available quantity', 'danger')
        return redirect(url_for('admin_request'))
    req.qty = request_quantity
    req.status = 1
    db.session.commit()
    flash('Request Accepted', 'success')
    return redirect(url_for('admin_request'))


#reject request
@app.route('/admin/request/delete/<int:req_id>', methods = ['POST'])
@login_required
def reject_request(req_id):
    if not current_user.isAdmin: abort(403) 
    req  = Request.query.get_or_404(req_id)
    req.status = -1
    db.session.commit()
    flash('Request rejected','success')
    return redirect(url_for('admin_request'))


# view all the processed request
@app.route('/admin/requests/summary')
@login_required
def admin_summary():
    if not current_user.isAdmin: abort(403) 
    requests = Request.query.all()[::-1]
    return render_template('admin_summary.html', requests = requests)



### Admin user management ###

@app.route('/admin/users')
@login_required
def display_users():
    if not current_user.isAdmin: abort(403) 
    users = User.query.all()
    return render_template('display_users.html', users = users)

@app.route('/admin/users/add', methods = ['GET', 'POST'])
@login_required
def add_users():
    if not current_user.isAdmin: abort(403) 
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user:
            flash(f"This email is already registered. Please try with another email id","info")
        else:
            password = bcrypt.generate_password_hash(form.password.data)
            user = User(
                first_name = form.first_name.data, 
                last_name = form.last_name.data,
                email = form.email.data, 
                password = password
                )
            db.session.add(user)
            db.session.commit()
            flash(f"User Added","success")
            return redirect(url_for('display_users'))
    return render_template('register.html',title = 'Register', form = form)

@app.route('/profile/<int:user_id>')
@login_required
def view_user(user_id):
    if not current_user.isAdmin: abort(403)
    user = User.query.get_or_404(user_id)
    return render_template('view_user.html', user = user)

@app.route('/profile/update/password/<int:user_id>', methods = ['GET', 'POST'])
@login_required
def admin_update_password(user_id):
    if not current_user.isAdmin: abort(403)
    user = User.query.get_or_404(user_id)
    form = UpdatePassword()
    if form.validate_on_submit():
        if not bcrypt.check_password_hash(current_user.password, form.prev_password.data): 
            flash(f'Incorrect Password', 'danger')
        else:
            user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash(user.first_name + "'s Password was Updated", 'success')
    return render_template('update_password.html', form = form, user = user)

@app.route('/profile/delete/account/<int:user_id>', methods = ['POST'])
@login_required
def admin_delete_account(user_id):
    if not current_user.isAdmin: abort(403)
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("Account Deleted", 'success')
    return redirect(url_for('display_users'))

@app.route('/profile/toggleadmin/<int:user_id>', methods = ['POST'])
@login_required
def toggle_admin(user_id):
    if not current_user.isAdmin: abort(403)
    user = User.query.get_or_404(user_id)
    user.isAdmin = not user.isAdmin
    db.session.commit()
    flash("Account Updated", 'success')
    return redirect(url_for('view_user', user_id = user.id))

@app.route('/profile/togglesuperuser/<int:user_id>', methods = ['POST'])
@login_required
def toggle_superuser(user_id):
    if not current_user.isAdmin: abort(403)
    user = User.query.get_or_404(user_id)
    user.isAdmin = not user.isAdmin
    user.isSuperUser = not user.isSuperUser
    db.session.commit()
    flash("Account Updated", 'success')
    return redirect(url_for('view_user', user_id = user.id))
    
    


# ----------------- User routes ------------------



# User request routes 

# View all the stocks
@app.route('/user/home', methods=['GET', 'POST'])
@login_required
def user_home():
    stocks = Stock.query.all()
    quota = []
    for stock in stocks:
        requests = Request.query.filter_by(user_id = current_user.id, stock_id= stock.id).all()
        temp = 0
        for i in requests:
            if i.status == 0 or i.status == 1:
                temp += i.qty
        quota_left = max(0, stock.quota - temp)
        quota.append(quota_left)

    return render_template("user.html", stocks = stocks, quota = quota, length = len(quota))


# Make a request for a stock
@app.route('/make/request/<int:stock_id>', methods=['GET', 'POST'])
@login_required
def make_request(stock_id):
    form = RequestForm()
    stock = Stock.query.get_or_404(stock_id)
    if form.validate_on_submit():
        requests = Request.query.filter_by(user_id = current_user.id, stock_id= stock.id).all()
        temp = 0
        for i in requests:
            if i.status == 0 or i.status == 1:
                temp += i.qty
        quota_left = max(0, stock.quota - temp)
        if quota_left >= form.quantity_req.data:
            request = Request(
                user_id = current_user.id,
                stock_id=stock.id,
                qty = form.quantity_req.data,
                users_comment = form.message.data,
                original_quantity = form.quantity_req.data
            )
            db.session.add(request)
            db.session.commit()
            flash('Request Made Successfully', 'success')
            print('Request Sucessful')
        else:
            print('Quota exceeded')
            flash('You cannot request more than the available quota', 'danger')
    return render_template('request_stock.html', form=form, stock=stock)

# Confirm that you have received the item
@app.route('/user/requests/received/<int:request_id>', methods=['POST'])
@login_required
def request_received(request_id):
    req = Request.query.get_or_404(request_id)
    if current_user.id != req.user_id:  abort(403)
    req.accepted = True
    req.received_comment = str(request.form['textarea'])
    db.session.commit()
    flash('Request Updated')
    return redirect(url_for('user_summary'))


# View categories of the stocks
@app.route('/categories')
def categories():
    cat = Category.query.all()
    return render_template('categories.html', categories = cat)

# view all the stocks of a category 
@app.route('/categories/<int:category_id>')
def category(category_id):
    stocks = Stock.query.filter_by(category_id = category_id).all()
    quota = []
    for stock in stocks:
        requests = Request.query.filter_by(user_id = current_user.id, stock_id= stock.id).all()
        temp = 0
        for i in requests:
            if i.status == 0 or i.status == 1:
                temp += i.qty
        quota_left = max(0, stock.quota - temp)
        quota.append(quota_left)
    return render_template('user.html', stocks= stocks, quota = quota, length = len(quota))

# view the summary of all the requests that you have made
@app.route('/user/request/summary')
@login_required
def user_summary():
    requests = User.query.get(current_user.id).requests[::-1]
    return render_template('summary.html', requests = requests)




#---------------- General Routes --------------------

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/profile')
@login_required
def account():
    return render_template('account.html')

@app.route("/profile/update", methods=['POST', 'GET'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if not bcrypt.check_password_hash(current_user.password, form.password.data): 
            flash(f'Incorrect Password', 'danger')
        else:
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.email = form.email.data
            image_name = current_user.picture
            if form.picture.data:
                image_name = save_picture(form.picture.data, 'profile')
            current_user.picture = image_name
            db.session.commit()
            flash('Account was Updated', 'success')
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email
    return render_template('profile.html', form = form)

@app.route("/profile/update/password", methods=['POST', 'GET'])
@login_required
def update_password():
    form = UpdatePassword()
    if form.validate_on_submit():
        if not bcrypt.check_password_hash(current_user.password, form.prev_password.data): 
            flash(f'Incorrect Password', 'danger')
        else:
            current_user.password = bcrypt.generate_password_hash(form.password.data)
            db.session.commit()
            flash('Password was Updated', 'success')
    return render_template('update_password.html', form = form)



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
            flash(f'Welcome {current_user.first_name}!', 'success')
            return redirect(next_page) if next_page else  redirect(url_for('home'))
        else:
            flash(f"Your login credentials don't match", 'danger')
    
        
    return render_template('login.html',form = form)

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))



############# utils ####################
def save_picture(form_picture, folder):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path , 'static/images/' + folder + "/" , picture_fn)
    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn