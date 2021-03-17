# FastAPI provides auto validation and auto documentation of the vars with pydentic lib

from fastapi import FastAPI
from models.user import User
from models.book import Book
from models.author import Author

app = FastAPI()

#For LogIn System
@app.post("/user")
async def post_user(user: User):
    return {"Request body": user}
# when you forward parameters under get method no need to add ?: /user?param
@app.get("/user")
async def get_user_validation(password: str):
    return {"Query param": password}

# when you take variable parameter you should put it in {}
@app.get("/book/{isbn}")
async def get_book_with_isbn(isbn: str):
    return {"Query isbn var": isbn}