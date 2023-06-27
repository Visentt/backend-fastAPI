from fastapi import APIRouter

route = APIRouter(prefix="/products", tags=["products"] , responses={404:{"Message":"No encontrado"}})

products = ["Product1","Product2","Product3","Product4"]

@route.get("/")
async def return_products():
    return {"productos":products}

@route.get("/{id}")
async def return_products(id : int):
    return {"prosucto":products[id-1]}