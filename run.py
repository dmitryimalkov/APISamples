# FastAPI provides auto validation and auto documentation of the vars with pydentic lib

from fastapi import FastAPI
from models.user import User
app = FastAPI()

#For LogIn System
@app.post("/user")
async def post_user(user: User):
    return {"Request body": user}

