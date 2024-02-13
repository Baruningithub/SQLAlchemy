from main import user,Session

s2=Session()

user_to_delete =s2.query(user).filter(user.email=="mail@3ty").first()

s2.delete(user_to_delete)

s2.commit()