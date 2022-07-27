import redis
import time
r = redis.Redis(host='localhost', port=6379)
r.psetex("NAME", 1000, "Hi")
print(r.get("NAME"))
r.mset({"Germany": "Berline", "France": "Paris"})