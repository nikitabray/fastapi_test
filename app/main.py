from fastapi import FastAPI, Body


app = FastAPI()

names = []

@app.get("/multiply/")
async def mult(a: int = 1, b: int = 2):
        return {"result": a * b}


@app.post("/add_name/")
async def add_name(name: str = Body(...)):
        names.append(name)
        return names
