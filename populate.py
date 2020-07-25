from App import db
from App.models import User, Stock, Request, Category

db.create_all()

categories = [

    Category(
        id = 1,
        name = 'Paper Products',
    ),

    Category(
        id = 2,
        name = 'Writing Material'
    ),

    Category(
        id = 3,
        name = 'Desk Item'
    ),


    Category(
        id = 4,
        name = 'File / Folder'
    ),


    Category(
        id = 5,
        name = 'Art / Crafts'
    ),

    Category(
        id = 6,
        name = 'Cleaning Material'
    ),

    Category(
        id = 7,
        name = 'Coputer Pheripherals'
    ),
]


stocks = [
    Stock(
        item = 'Box File',
        category_id = 4,
        qty_prev = 4, 
        avail = 100, 
        qty_req = 0, 
        qty_pres = 0,
        maximum_limit = 5,
        minimum_limit=1,
        quota = 20,
    ),
]



for cat in categories:
    db.session.add(cat)
    db.session.commit()

for stock in stocks:
    db.session.add(stock)
    db.session.commit()



user = User(
    email = 'jaideep.more@somaiya.edu', 
    first_name = 'Jaideep', 
    last_name = 'More', 
    password = b'$2b$12$SkeGMWqz.UGYxguj3j2LNOtN5nfvfRrqtS43dybKWJIBUtPR64Ezm',
    isAdmin = True,
    isSuperUser = False,
)
db.session.add(user)
db.session.commit()

user = User(
    email = 'vedant.manelkar@somaiya.edu', 
    first_name = 'Vedant', 
    last_name = 'Manelkar', 
    password = b'$2b$12$SkeGMWqz.UGYxguj3j2LNOtN5nfvfRrqtS43dybKWJIBUtPR64Ezm',
    isAdmin = False,
    isSuperUser = False,
)
db.session.add(user)
db.session.commit()

user = User(
    email = 'keshav.sm@somaiya.edu', 
    first_name = 'Keshav', 
    last_name = 'Mishra', 
password = b'$2b$12$SkeGMWqz.UGYxguj3j2LNOtN5nfvfRrqtS43dybKWJIBUtPR64Ezm',
    isAdmin = True,
    isSuperUser = True,
)
db.session.add(user)
db.session.commit()


