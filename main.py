from imports import *

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')
base=declarative_base()
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)


class user(base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(35), nullable=False)
    email = Column(String(59), unique=True)
    date_created = Column(DateTime(), default=datetime.now) 
    addresses = relationship("Address", back_populates="users")   
    def __repr__(self):
        return f"<id: {self.id} Name: {self.name} email:{self.email} date_created: {self.date_created}>"

class Address(base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True,autoincrement=True)
    address = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship("user", back_populates="addresses")
    
base.metadata.create_all(engine)

