import os

import redis.asyncio as redis
from dotenv import load_dotenv
from redis.asyncio.client import Redis

load_dotenv()

REDIS_HOST = os.environ.get("REDIS_HOST", "redis")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
CACHE_TIME = int(os.environ.get("CACHE_TIME", 60 * 60 * 10))

redis_client : Redis = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)
