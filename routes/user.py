from fastapi import APIRouter, Response, status
from config.db import connection
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/users", response_model = list[User], response_description = "List the users that were uploaded to the database", tags = ["users"])
def get_users():
    return connection.execute(users.select()).fetchall()


@user.post("/users", response_model = User, response_description = "Create a new user", tags = ["users"])
def create_user(user: User):
    new_user = {"name": user.name, "email": user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = connection.execute(users.insert().values(new_user))
    return connection.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.get("/users/{id}", response_model = User, response_description = "Get a user from its id", tags = ["users"])
def get_user(id: str):
    return connection.execute(users.select().where(users.c.id == id)).first()


@user.delete("/users/{id}", status_code = status.HTTP_204_NO_CONTENT, response_description = "Delete a user from its id", tags = ["users"])
def delete_user(id: str):
    connection.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@user.put("/users/{id}", response_model = User, response_description = "Update a user from its id. Change the fields you want to renew and complete the others with the previous values.", tags = ["users"])
def update_user(id: str, user: User):
    connection.execute(users.update().values(
        name=user.name, email=user.email, password=f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return connection.execute(users.select().where(users.c.id == id)).first()
