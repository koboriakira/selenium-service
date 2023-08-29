from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.scraping import Scraping

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class RequestTwitterModel(BaseModel):
    url: str = Field(..., description="スクレイピング対象のTwitterのURL",
                     regex="http.?://(x|twitter)\.com.*")


class ResponseModel(BaseModel):
    url: str = Field(..., description="スクレイピング対象のURL", regex="http.?://.*")
    content: str = Field(..., description="スクレイピング結果")


@app.post("/twitter")
async def scrape_twitter(request: RequestTwitterModel):
    scraping = Scraping()
    result = scraping.scrape_twitter(request.url)
    return {
        "url": request.url,
        "content": result
    }
