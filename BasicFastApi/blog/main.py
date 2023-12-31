from fastapi import FastAPI
from schemas import Blog

# from . import models
# from pydantic import BaseModel

app = FastAPI()

# models.Base.metadata.create_all()

# #pydantic model
# class Blog(BaseModel):
#     title: str
#     body: str

# @app.post('/blog')
# def create(title,body):
#     return {'title': title, 'body': body}
@app.post('/blog')
def create(request: Blog):
    return request