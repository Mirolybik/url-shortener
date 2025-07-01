import redis.asyncio as redis
import secrets
from typing import Optional
from app.config import settings

class URLShortener:
    def __init__(self):
        self.redis = redis.Redis(host="redis", port=6379, db=0)

    async def shorten(self, original_url: str) -> dict:
        for i in range(5):
            short_key = secrets.token_urlsafe(settings.SHORT_URL_LENGTH)[:settings.SHORT_URL_LENGTH]
            if not await self.redis.exists(short_key):
                await self.redis.setex(short_key, settings.DEFAULT_TTL, str(original_url))
                return {
                    "short_url": f"http://localhost:8000/{short_key}",
                    "original_url": str(original_url),
                    "expires_in": settings.DEFAULT_TTL
                }
        raise ValueError("key error")

    async def get_original(self, short_key: str) -> Optional[str]:
        return await self.redis.get(short_key)

    async def delete(self, short_key: str):
        await self.redis.delete(short_key)