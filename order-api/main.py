from fastapi import FastAPI

app = FastAPI()

@app.get("/order")
async def get_order():
    return {"order": 12345}
