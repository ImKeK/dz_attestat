from fastapi import FastAPI
from seminar6.d_b import database
from seminar6.rout import user, product, order, data

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(user.router, tags=["users"])
app.include_router(product.router, tags=["products"])
app.include_router(order.router, tags=["orders"])
app.include_router(data.router, tags=["data"])