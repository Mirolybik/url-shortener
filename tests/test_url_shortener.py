import pytest
import httpx
import asyncio
from services.url_shortener import URLShortener

@pytest.mark.asyncio
async def test_shorten_url():
    shortener = URLShortener()
    result = await shortener.shorten("https://example.com ")
    assert result["short_url"].startswith("http://localhost:8000/")
    assert len(result["short_url"].split("/")[-1]) == 6

@pytest.mark.asyncio
async def test_redirect():
    shortener = URLShortener()
    result = await shortener.shorten("https://example.com ")
    short_key = result["short_url"].split("/")[-1]
    original = await shortener.get_original(short_key)
    assert original == "https://example.com "

@pytest.mark.asyncio
async def test_delete_url():
    shortener = URLShortener()
    result = await shortener.shorten("https://example.com ")
    short_key = result["short_url"].split("/")[-1]
    await shortener.delete(short_key)
    assert await shortener.get_original(short_key) is None