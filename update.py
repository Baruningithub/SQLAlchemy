from main import user,Session

s2=Session()

user_to_uptdate =s2.query(user).filter(user.name=="Barun").first()

user_to_uptdate.name = "Barun Hazary"
user_to_uptdate.email= "offficial@amil.com"

print(user_to_uptdate)

s2.commit()