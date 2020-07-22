from App import db
from App.models import User, Stock, Request

db.create_all()

stock1 = Stock(
    item = 'Box File',
    qty_prev = 4, 
    avail = 100, 
    qty_req = 0, 
    qty_pres = 0,
    maximum_limit = 5,
    minimum_limit=1,
    quota = 20,
)

stock2 = Stock(
    item = 'Register', 
    qty_prev = 4, 
    avail = 100, 
    qty_req = 0, 
    qty_pres = 0,
    maximum_limit = 5,
    minimum_limit=1,
    quota = 20,
)

stock3 = Stock(
    item = 'Whitener', 
    qty_prev = 4,
    avail = 100, 
    qty_req = 0, 
    qty_pres = 0,
    maximum_limit = 5,
    minimum_limit=1,
    quota = 20,
)

stock4 = Stock(
    item = 'Tissue Paper', 
    qty_prev = 4, 
    avail = 100, 
    qty_req = 0, 
    qty_pres = 0,
    maximum_limit = 5,
    minimum_limit=1,
    quota = 20,
)

stock5 = Stock(
    item = 'Chalk Box', 
    qty_prev = 4, 
    avail = 100, 
    qty_req = 0, 
    qty_pres = 0,
    maximum_limit = 5,
    minimum_limit=1,
    quota = 20,
)

db.session.add(stock1)
db.session.add(stock2)
db.session.add(stock3)
db.session.add(stock4)
db.session.add(stock5)

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

# req1 = Request(
#     user_id = 1,
#     stock_id= 1,
#     qty = 3,
#     users_comment = "Please Send immediately",
#     admins_comment = "How Dare You"
# )

# req2 = Request(
#     user_id = 1,
#     stock_id= 3,
#     qty = 3,
#     users_comment = "Please Send immediately",
#     admins_comment = "How Dare You"
# )

# req3 = Request(
#     user_id = 2,
#     stock_id= 2,
#     qty = 3,
#     users_comment = "Please Send immediately",
#     admins_comment = "How Dare You"
# )

# req4 = Request(
#     user_id = 3,
#     stock_id= 1,
#     qty = 3,
#     users_comment = "Please Send immediately",
#     admins_comment = "How Dare You"
# )

# db.session.add(req1)
# db.session.add(req2)
# db.session.add(req3)
# db.session.add(req4)

# db.session.commit()
