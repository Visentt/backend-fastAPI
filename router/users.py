from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

route = APIRouter(prefix="/users", tags=["users"] , responses={404:{"Message":"No encontrado"}})

class User(BaseModel):
    id : int
    name : str
    surname : str
    url : str
    age: int
        
users = [User(id =1,name="Victor",surname= "visente",url="http://visent",age = 18),User(id = 2,name="Mauricio",surname="mauro",url= "http://mauro",age = 18)]

@route.get("/")
async def Users():
    return users

@route.get("/{id}", response_model=User ,status_code=200)
async def Users(id:int):
    for i in users:
        if i.id == id:
            return i
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@route.post("/", response_model=User, status_code=201)
async def insert_user(user : User):
    for i in users:
        if i.id == user.id:
            raise HTTPException(status_code=404, detail="El usuario ya existe")
    users.append(user)
    return user    

@route.put("/", response_model=User,status_code=201)
async def update_user(user : User):
    exist_user = False
    for index, i in enumerate(users):
        if i.id == user.id:
            users[index] = user
            exist_user = True
            return user
    if not exist_user:    
        raise HTTPException(status_code=404, detail="El usuario no existe")
    
@route.delete("/{id}", response_model=User,status_code=200)
async def delete_user(id : int):
    exist_user = False
    for index, i in enumerate(users):
        if i.id == id:
            del users[index] 
            exist_user = True
            return i
    if not exist_user:    
        raise HTTPException(status_code=404, detail="El usuario no existe")