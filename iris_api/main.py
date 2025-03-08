from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}

@app.get("/healthcheck2")
def healthcheck2():
    return {"status": "ok"}