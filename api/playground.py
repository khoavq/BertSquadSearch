import redis

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
redis_db.flushall()
print(redis_db.keys())

