import redis

redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)
redis_db.flushall()

redis_db.hset("q", "score", 1)
redis_db.hset("q", "question", "this is question")

a = {
    "ans": "yes"
}

r = redis_db.hgetall("q")
print(redis_db.hget("q", "score").decode("utf-8"))
