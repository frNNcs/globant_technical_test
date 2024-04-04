import os

import redis.asyncio as redis
from dotenv import load_dotenv
from redis.asyncio.client import Redis

load_dotenv()

REDIS_URL = os.environ.get("REDIS_URL", "redis://redis:6379")
CACHE_TIME = int(os.environ.get("CACHE_TIME", 60 * 60 * 10))

redis_client : Redis = redis.Redis(
    host='redis',
    port=6379,
    decode_responses=True
)
