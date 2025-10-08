from redis.asyncio import Redis
from config import settings
from typing import Optional, Any
import json

# Global Redis client
redis_client: Optional[Redis] = None


async def init_redis() -> Redis:
    """
    Initialize Redis connection
    """
    global redis_client
    
    redis_client = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD,
        decode_responses=True,
        encoding="utf-8",
        max_connections=50
    )
    
    # Test connection
    await redis_client.ping()
    print("Redis initialized successfully")
    return redis_client


async def close_redis():
    """
    Close Redis connection
    """
    global redis_client
    if redis_client:
        await redis_client.close()
        print("Redis connection closed")


async def get_redis() -> Redis:
    """
    Dependency function to get Redis client
    Usage: redis: Redis = Depends(get_redis)
    """
    return redis_client


class CacheService:
    """
    Cache service helper class for common Redis operations
    """
    
    @staticmethod
    async def get(key: str) -> Optional[str]:
        """Get value from cache"""
        if redis_client:
            return await redis_client.get(key)
        return None
    
    @staticmethod
    async def set(key: str, value: Any, expire: int = 3600) -> bool:
        """Set value in cache with expiration (default 1 hour)"""
        if redis_client:
            if not isinstance(value, str):
                value = json.dumps(value)
            return await redis_client.setex(key, expire, value)
        return False
    
    @staticmethod
    async def delete(key: str) -> bool:
        """Delete key from cache"""
        if redis_client:
            return bool(await redis_client.delete(key))
        return False
    
    @staticmethod
    async def exists(key: str) -> bool:
        """Check if key exists in cache"""
        if redis_client:
            return bool(await redis_client.exists(key))
        return False
    
    @staticmethod
    async def get_json(key: str) -> Optional[dict]:
        """Get JSON value from cache"""
        value = await CacheService.get(key)
        if value:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return None
        return None
    
    @staticmethod
    async def incr(key: str, amount: int = 1) -> int:
        """Increment value in cache"""
        if redis_client:
            return await redis_client.incrby(key, amount)
        return 0
    
    @staticmethod
    async def expire(key: str, seconds: int) -> bool:
        """Set expiration on key"""
        if redis_client:
            return await redis_client.expire(key, seconds)
        return False

