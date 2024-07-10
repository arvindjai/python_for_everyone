from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World!"}

@app.get("/posts")
def posts():
    return {"Posts": "Here is my post"}

# @app.post("/")
# def get_post():
