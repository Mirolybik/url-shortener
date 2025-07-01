from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
from typing import Optional
import httpx
import asyncio
from app.services.url_shortener import URLShortener
from app.config import settings

app = FastAPI(title="URL Shortener")
shortener = URLShortener()

class URLRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    short_url: str
    original_url: str
    expires_in: Optional[int] = None

@app.post("/shorten", response_model=URLResponse)
async def shorten_url(request: URLRequest):
    short_url = await shortener.shorten(request.url)
    return short_url

@app.get("/{short_key}", response_class=RedirectResponse)
async def redirect_to_url(short_key: str):
    original_url = await shortener.get_original(short_key)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return original_url

@app.delete("/{short_key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(short_key: str):
    await shortener.delete(short_key)
    return {"status": "success"}