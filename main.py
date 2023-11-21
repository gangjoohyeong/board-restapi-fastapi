from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from api import article_api

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/", tags=["root"])
def hello() -> dict:
    return {"message": "Hello World"}

app.include_router(article_api.router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)