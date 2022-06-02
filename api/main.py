from fastapi import FastAPI
from .routes import users
from .routes import students

app = FastAPI()

app.include_router(users.router)
app.include_router(students.router)