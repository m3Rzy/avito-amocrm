# from typing import Union
from fastapi import HTTPException
from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def read_root():
    response = requests.get("https://api.vk.com/method/users.get?user_id=210700286&v=5.131")
    if response.status_code == 200:
        return response.json()
    else:
        print(response.json)
        raise HTTPException(status_code=400, detail="Ошибка в запросе!")


# uvicorn main:app --reload