from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.scraping import Scraping

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class RequestModel(BaseModel):
    url: str = Field(..., description="スクレイピング対象のURL", regex="http.?://.*")


class ResponseModel(BaseModel):
    url: str = Field(..., description="スクレイピング対象のURL", regex="http.?://.*")
    content: str = Field(..., description="スクレイピング結果")


@app.post("/")
async def root(request: RequestModel):
    scraping = Scraping()
    result = scraping.scrape(request.url)
    print(result)

    return {
        "url": request.url,
        "content": "Hello World"
    }
