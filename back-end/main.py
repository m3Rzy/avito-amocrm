# from typing import Union
from fastapi import HTTPException
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import requests

app = FastAPI()

client_id = "DoUdME3uqicpqcjLDFby"
client_secret = "x6bRjFWQ92EbqzaxmgKI3GgLqCb1ZbQ2XVB6WkiT"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.post("/")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token' : form_data.username + 'token'}

@app.get("/")
async def index(token: str = Depends(oauth2_scheme)):
    return {'the_token' : token}
