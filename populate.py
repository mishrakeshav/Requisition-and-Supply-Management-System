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
        item = 'Long Register (140 Pages)',
        category_id = 1,
        qty_prev = 12,
        avail = 5,
        qty_req = 0, 
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Long Register (68 Pages)',
        category_id = 1,
        qty_prev = 24,
        avail = 10,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'A4 Size Printing Paper (Ream)',
        category_id = 1,
        qty_prev = 24,
        avail = 2,
        qty_req = 24,
        qty_pres = 0,
        maximum_limit = 7,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Blank Plan Paper',
        category_id = 1,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 10,
        minimum_limit=5,
        quota = 20,
    ),
Stock(
        item = 'Dot Matrix Printing Paper',
        category_id = 1,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 10,
        minimum_limit=5,
        quota = 20,
    ),
Stock(
        item = 'White Board Marker (Blue)',
        category_id = 2,
        qty_prev = 0,
        avail = 0,
        qty_req = 30,
        qty_pres = 0,
        maximum_limit = 11,
        minimum_limit=6,
        quota = 20,
    ),
Stock(
        item = 'White Board Marker (Black)',
        category_id = 2,
        qty_prev = 0,
        avail = 0,
        qty_req = 30,
        qty_pres = 0,
        maximum_limit = 11,
        minimum_limit=6,
        quota = 20,
    ),
Stock(
        item = 'White Board Marker (Red)',
        category_id = 2,
        qty_prev = 0,
        avail = 0,
        qty_req = 10,
        qty_pres = 0,
        maximum_limit = 11,
        minimum_limit=6,
        quota = 20,
    ),
Stock(
        item = 'White Board Marker (Green)',
        category_id = 2,
        qty_prev = 0,
        avail = 0,
        qty_req = 10,
        qty_pres = 0,
        maximum_limit = 11,
        minimum_limit=6,
        quota = 20,
    ),
Stock(
        item = 'Permanent Marker',
        category_id = 2,
        qty_prev = 0,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 7,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Paper Pin Box (Small)',
        category_id = 3,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Stapler Pin Small (Big Box)',
        category_id = 3,
        qty_prev = 0,
        avail = 0,
        qty_req = 1,
        qty_pres = 0,
        maximum_limit = 6,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Stapler Pin Big (Big Box)',
        category_id = 3,
        qty_prev = 0,
        avail = 0,
        qty_req = 1,
        qty_pres = 0,
        maximum_limit = 6,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'U Pin Box (Small)',
        category_id = 3,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'U Pin Box (Big)',
        category_id = 3,
        qty_prev = 4,
        avail = 100,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 5,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Box File',
        category_id = 4,
        qty_prev = 4,
        avail = 0,
        qty_req = 30,
        qty_pres = 0,
        maximum_limit = 15,
        minimum_limit=10,
        quota = 20,
    ),
Stock(
        item = 'Spring File',
        category_id = 4,
        qty_prev = 0,
        avail = 0,
        qty_req = 12,
        qty_pres = 0,
        maximum_limit = 15,
        minimum_limit=10,
        quota = 20,
    ),
Stock(
        item = 'Ring File',
        category_id = 4,
        qty_prev = 0,
        avail = 0,
        qty_req = 30,
        qty_pres = 0,
        maximum_limit = 15,
        minimum_limit=10,
        quota = 20,
    ),
Stock(
        item = 'Plastic File',
        category_id = 4,
        qty_prev = 0,
        avail = 0,
        qty_req = 20,
        qty_pres = 0,
        maximum_limit = 10,
        minimum_limit=5,
        quota = 20,
    ),
Stock(
        item = 'Four Flap File',
        category_id = 4,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 6,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Sketch Pen',
        category_id = 5,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Highlighter Diff. Colour',
        category_id = 5,
        qty_prev = 0,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Stapler (Kangaroo) Big',
        category_id = 5,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Stapler (Kangaroo) Small',
        category_id = 5,
        qty_prev = 0,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Punching Machine (Big)',
        category_id = 5,
        qty_prev = 0,
        avail = 0,
        qty_req = 2,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Brush (for Key Board Cleaning)',
        category_id = 6,
        qty_prev = 0,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Cloth Duster',
        category_id = 6,
        qty_prev = 0,
        avail = 0,
        qty_req = 30,
        qty_pres = 0,
        maximum_limit =21,
        minimum_limit=20,
        quota = 20,
    ),
Stock(
        item = 'Cloth Duster (Yellow for Computer Cleaning)',
        category_id = 6,
        qty_prev = 0,
        avail = 0,
        qty_req = 25,
        qty_pres = 0,
        maximum_limit = 21,
        minimum_limit=20,
        quota = 20,
    ),
Stock(
        item = 'Quid Hand Wash with Dispenser (Dettol)',
        category_id = 6,
        qty_prev = 5,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'Apron',
        category_id = 6,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'Extension Socket ',
        category_id = 7,
        qty_prev = 0,
        avail = 0,
        qty_req = 2,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'cable tai big size 16 inch',
        category_id = 7,
        qty_prev = 0,
        avail = 0,
        qty_req = 5,
        qty_pres = 0,
        maximum_limit = 3,
        minimum_limit=2,
        quota = 20,
    ),
Stock(
        item = 'CD Pouch (for 50 CD)',
        category_id = 7,
        qty_prev = 0,
        avail = 0,
        qty_req = 0,
        qty_pres = 0,
        maximum_limit = 2,
        minimum_limit=1,
        quota = 20,
    ),
Stock(
        item = 'HP Lasrerjet p1108 -3 canon 2900-2 Cartridge-1',
        category_id = 7,
        qty_prev = 2,
        avail = 0,
        qty_req = 3,
        qty_pres = 0,
        maximum_limit = 6,
        minimum_limit=5,
        quota = 20,
    ),
Stock(
        item = 'HP Lasrerjet p1108 -3 canon 2900-2 Cartridge-2',
        category_id = 7,
        qty_prev = 2,
        avail = 0,
        qty_req = 2,
        qty_pres = 0,
        maximum_limit = 6,
        minimum_limit=5,
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

