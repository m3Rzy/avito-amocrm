# from typing import Union
from fastapi import HTTPException
import requests
from fastapi import FastAPI, Depends
from urllib.parse import urlencode
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

def post_token():
    the_data = {
    "client_id": "DoUdME3uqicpqcjLDFby",
    "client_secret": "x6bRjFWQ92EbqzaxmgKI3GgLqCb1ZbQ2XVB6WkiT",
    "grant_type": "client_credentials"
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://api.avito.ru/token/", data=the_data, headers=headers)
    return response.json()["access_token"]

@app.get("/token")
def get_token():
    return post_token()

@app.get("/getchats")
def get_chats():
    bearer = "Bearer " + post_token()
    headers2 = {"Authorization": bearer}
    response2 = requests.get("https://api.avito.ru/messenger/v2/accounts/304053114/chats", headers=headers2)
    return response2.json()