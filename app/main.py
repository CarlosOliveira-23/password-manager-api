from fastapi import FastAPI

app = FastAPI(title="Password Manager API", version="1.0")


@app.get("/")
def read_root():
    return {"message": "Password Manager API is running!"}


app.include_router(auth.router, prefix="/auth")