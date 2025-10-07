from fastapi import FastAPI
# This is update1
app = FastAPI()

@app.get("/order")
async def get_order():
    return {"order": 12345}
