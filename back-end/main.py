from fastapi import HTTPException
import requests
from fastapi import FastAPI, Depends
from urllib.parse import urlencode
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


class Text(BaseModel):
    text: str

class Message(BaseModel):
    message: Text
    type_: str = "text"
    class Config:
        fields = {
            'type_': 'type'
        }


app = FastAPI()


def post_token():
    the_data = {
        "client_id": "DoUdME3uqicpqcjLDFby",
        "client_secret": "x6bRjFWQ92EbqzaxmgKI3GgLqCb1ZbQ2XVB6WkiT",
        "grant_type": "client_credentials"
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(
        "https://api.avito.ru/token/", data=the_data, headers=headers)
    return response.json()["access_token"]


@app.get("/token")
def get_token():
    return post_token()


@app.get("/getchats")
def get_chats():
    bearer = "Bearer " + post_token()
    headers2 = {"Authorization": bearer}
    response2 = requests.get(
        "https://api.avito.ru/messenger/v2/accounts/304053114/chats", headers=headers2)
    return response2.json()["chats"][0]


@app.get("/getchats/id")
def get_custom_chat():
    return get_chats()["id"]


@app.get("/getchats/user_id")
def get_custom_user_id():
    return get_chats()["users"][1]["id"]


chat_id = get_custom_chat()
user_id = get_custom_user_id()

print(chat_id)
print(user_id)



@app.post("/send")
def send_chat(user_id: int, chat_id: str, message:Message):
    bearer = "Bearer " + post_token()
    headers = {"Authorization": bearer, 'Content-Type': 'application/json'}
    response = requests.post(
        f"https://api.avito.ru/messenger/v1/accounts/{user_id}/chats/{chat_id}/messages", headers=headers, json=jsonable_encoder(message))
    return response.json()
