from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
async def get_user():
    return {"user": "Alice"}
