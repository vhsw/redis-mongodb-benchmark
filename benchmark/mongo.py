from pymongo import MongoClient
from benchmark.common import basic_fields

client = MongoClient("mongodb://root:pass@localhost")
db = client.name
collection = db.urls


def put(data):
    collection.insert_one(data)


def get_keys():
    return [
        document["url"]
        for document in collection.find({"url": {"$exists": True}}, projection={"url"})
    ]


def get_basic(url):
    return collection.find_one({"url": url}, projection=basic_fields)


def get_full(url):
    return collection.find_one({"url": url})
