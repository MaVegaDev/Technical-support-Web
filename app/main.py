from fastapi import FastAPI

app = FastAPI(title="Service Order System")

@app.get("/")
def root():
    return {"message" : "Hello world"}