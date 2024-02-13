from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os

# BASE_DIR = os.path.dirname(os.path.realpath(__file__))

pswd='sql_pswd1'
host='172.16.8.107'
username='aiml'
port='3306'
db1='practice'
connection_string = f'mysql://{username}:{pswd}@{host}:{port}/{db1}'
base=declarative_base()
engine = create_engine(connection_string)

class user(base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String(35),nullable=False)
    email = Column(String(59),unique=True)
    date_created = Column(DateTime(),default=datetime.now)    
    def __repr__(self):
        return f"<id: {self.id} Name: {self.name} email:{self.email} date_created: {self.date_created}>"
    
base.metadata.create_all(engine)

# new_user=user(id=1,name='BArun',email='mail@email')

# print(new_user)

# Session = sessionmaker(bind=engine)
# session = Session()

# result = engine.execute("SELECT * FROM AIML")

# # Fetch the results
# for row in result:
#     print(row)