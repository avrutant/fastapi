from fastapi import FastAPI

from Routes.user import user

app = FastAPI()
app.include_router(user)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
