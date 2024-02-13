from main import user,Address,Session

# join function
def join(session, user_id):   
   
    join_condition = (user.id == Address.user_id,)

   
    joined_query = (
        session.query(user.name,Address.address)
        .join(Address, *join_condition)
        .filter(user.id == user_id)
        .first()
    )

    return joined_query


local_session = Session()


userid = int(input("Enter user id: "))


result = join(local_session, userid)


if result:
    name, address = result
    print(f"id: {userid}, personname: {name}, address: {address}")
else:
    print(f"User with id {userid} not found.")

