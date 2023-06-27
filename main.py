from fastapi import FastAPI
from router import users, products
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.include_router(users.route)
app.include_router(products.route)
app.mount("/static", StaticFiles(directory="static"),"static")

@app.get("/")
async def home():
    return {"hello" : "hello"}

