from main import user,Session

s2=Session()

# users=s2.query(user).all()

ans =s2.query(user).filter(user.name=="Barun").first()

print(ans)