from main import user,Session
from sqlalchemy import desc

s2=Session()

# users=s2.query(user).all()

# users=s2.query(user).all()[1:] #limit

# users=s2.query(user).order_by(user.name).all() #odering

users=s2.query(user).order_by(desc(user.name)).all() #descending order

for u in users:
    print(u.name)
    print(u)