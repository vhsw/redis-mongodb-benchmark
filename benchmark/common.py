from faker import Faker
from faker.providers import internet, python


full_fields = {"text", "bsi", "keywords", "sentiment", "sentiment_values"}
basic_fields = {"bsi", "keywords", "sentiment"}

fake = Faker()
fake.add_provider(internet)
fake.add_provider(python)


def get_random_data():
    keywords = {fake.pystr(): fake.pyfloat() for _ in range(10)}
    return {
        "url": fake.url(),
        "text": fake.paragraph(nb_sentences=25),
        "bsi": fake.pyfloat(),
        "keywords": keywords,
        "sentiment": fake.random_element(["negative", "neutral", "positive"]),
        "sentiment_values": [fake.pyfloat(), fake.pyfloat(), fake.pyfloat()],
    }
