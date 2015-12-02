import redis

expToken = "7541a938-022f-4f91-8546-697552a39403"

results = {
    "response": 16.53423537256242,
    "waiting": 4.015143939856747,
    "avgCap": 17.882462745098067,
    "totalCap": 2682.3694117647096,
}

r = redis.Redis(host="localhost", port=6379, password="bighouse", db=2);

for key in results:
    r.hset(expToken, key, results[key])
