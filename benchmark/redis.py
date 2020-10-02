import json
from redis import Redis
from benchmark.common import full_fields, basic_fields

redis = Redis(
    password="pass",
    encoding="utf-8",
    decode_responses=True,
)


def put(data):
    mapping = {}
    for key in full_fields:
        if not isinstance(value := data[key], (bytes, str, int, float)):
            value = json.dumps(value)
        mapping[key] = value
    redis.hset(data["url"], mapping=mapping)


def get_keys():
    return redis.keys("http*")


def get_basic(url):
    data = dict(zip(basic_fields, redis.hmget(url, basic_fields)))
    data["keywords"] = json.loads(data["keywords"])
    return data


def get_full(url):
    data = redis.hgetall(url)
    data["keywords"] = json.loads(data["keywords"])
    return data
