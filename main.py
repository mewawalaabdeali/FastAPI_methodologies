from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello World, Welcome to the FASTAPI tutorial'}

@app.get("/about")
def about():
    return {'message':'CampusX is an educational platform where you can learn AI.'}