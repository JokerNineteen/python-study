# -*- coding: utf-8 -*-
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello Kitty"}

@app.get("/user/{username}")
async def read_user(username: str):
    return {"username": username}

@app.get("/search")
async def search(keyword: str = ""):
    return {"用户搜索了关键字": keyword}

@app.post("/login")
async def login(username: str, password: str):
    return {"username": username, "password": password}