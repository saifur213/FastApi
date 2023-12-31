from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# get operation----------------------
# path operation decorator (@app)
# decorate
@app.get('/') # base path
def index(): # path operation funtion
    return {'data': {'blog list'}}

@app.get('/blog')
def blog_list():
    return {'data': 'blog list'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}

# path parameter 
@app.get('/blog/{id}') # about path
def show(id: int):# path operation funtion
    # fetch blog with id = id
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data': {'1','2'}}

# Query Parameter --> we can set limit
@app.get('/blog2') # http://localhost:8000/blog2?limit=10 or http://localhost:8000/blog2?limit=50&published=true
def blog_list_2(limit=10, published: bool=True, sort: Optional[str] = None):
    # only get 10 published blog
    #return published
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}
    
@app.get('/blog2/{id}/comments')
def comments2(id, limit=10):
    # fetch comments of blog with id = id
    return limit
    return {'data': {'1','2'}}


# POST Method-------------------------------
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# Request Body
@app.post('/blog3')
def create_blog(blog: Blog):
    #return request
    return {'data': f"Blog is created with title as {blog.title}"}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)

