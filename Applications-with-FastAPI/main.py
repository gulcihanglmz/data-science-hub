from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "I'm Gülcihan", "ID":999}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": 1, "q": q}


'''
   dumps: Python nesnesini JSON formatına dönüştürür.
   loads: JSON formatındaki bir string'i Python nesnesine dönüştürür.
'''



