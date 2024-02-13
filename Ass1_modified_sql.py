from imports import *


class user_data(BaseModel):
    id : Union[int, None] = None
    name:str
    email: Union[str, None] = None
    date_created: Union[str, None] = None


app = FastAPI()


@app.post("/create")

async def create(new_user:user_data): 
    try:
        local_session = Session()
        new = user(name=new_user.name,email=new_user.email)

        local_session.add(new)
        
        local_session.commit()
        local_session.refresh(new)

        #json response
        return {"status": "success",
                "id" : new.id,
                "message": "Your account is succesfully created"
            }
    
    except IntegrityError as e:
        
        local_session.rollback()  
        error_message = str(e.orig) 
        raise HTTPException(status_code=400, detail=error_message)
    
    finally:
        local_session.close()


# get/print details of an existing user
@app.get("/get/{user_id}")
async def get(user_id):

    local_session = Session()
    u = local_session.query(user).filter(user.id==user_id).first()

    # Underflow check
    if not u:
        raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")
    
    local_session.close()

    return {"staus":"success",
            "Your account details are":u
    }


# updating details of an existing user
@app.patch("/update/{user_id}")
async def update(user_id, up_user:user_data):

    local_session = Session()

    user_to_uptdate =local_session.query(user).filter(user.id==user_id).first()
    # Underflow check
    if not user_to_uptdate:
        raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")
    
    local_session.query(user).filter(user.id==user_id).update(dict(up_user))

    local_session.commit()
    local_session.refresh(user_to_uptdate)

    local_session.close()

    return {"status": "success",
            "user_id":user_id,
            "message": "Your details are updated succesfully"
        }


# delete an existing user account
@app.delete("/delete/{user_id}")
async def delete(user_id):

    local_session = Session()
    user_to_del =local_session.query(user).filter(user.id==user_id).first()

    # Underflow check
    if not user_to_del:
        raise HTTPException(status_code=404, detail = f"No user with user id {user_id}")
    
    local_session.delete(user_to_del)
    local_session.commit()
    local_session.close()
    
    return {"status": "success",
            "user_id": user_id,
            "message": "Your account is now deleted"
        }



