from faker import Faker
from benchmark.mongo import put, get_basic, get_full, get_keys
from benchmark.common import get_random_data, basic_fields, full_fields
from random import choice

Faker.seed(0)
ROUNDS = 100


def test_mongo_put(benchmark):
    benchmark.pedantic(
        put,
        setup=lambda: ([get_random_data()], {}),
        rounds=ROUNDS,
        warmup_rounds=10,
    )


def test_mongo_get_basic(benchmark):
    result = benchmark.pedantic(
        get_basic,
        setup=lambda: ([choice(get_keys())], {}),
        rounds=ROUNDS,
        warmup_rounds=10,
    )
    for key in basic_fields:
        assert key in result


def test_mongo_get_full(benchmark):
    result = benchmark.pedantic(
        get_full,
        setup=lambda: ([choice(get_keys())], {}),
        rounds=ROUNDS,
        warmup_rounds=10,
    )
    for key in full_fields:
        assert key in result
