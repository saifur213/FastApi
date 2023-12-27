from fastapi import FastAPI

app = FastAPI()

#decorate
@app.get('/')
def index():
    return {'data': {'name': 'Saifur'}}

@app.get('/about')
def about():
    return {'data': {'about page'}}