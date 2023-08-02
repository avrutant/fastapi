from bson import ObjectId
from fastapi import APIRouter

from Configurations.db import conn
from Models.user import User
from Schemas.user import *

user = APIRouter()


@user.get('/')
async def find_all_users():
    return usersEntity(conn.demo.user.find())


@user.get('/{user_id}')
async def find_user(user_id:str):
    return usersEntity(conn.demo.user.find({"_id": ObjectId(user_id)}))


@user.post('/')
async def create_user(user: User):
    conn.demo.user.insert_one(dict(user))
    return usersEntity(conn.demo.user.find())


@user.put('/{id}')
async def update_user(id: str, user: User):
    conn.demo.user.update_one({"_id": ObjectId(id)}, {"$set": dict(user)})
    return usersEntity(conn.demo.user.find({"_id": ObjectId(id)}))


@user.delete('/{id}')
async def update_user(id: str, user: User):
    conn.demo.user.delete_one({"_id": ObjectId(id)})
    return usersEntity(conn.demo.user.find())
