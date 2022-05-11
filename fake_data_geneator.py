import sqlite3
from random import randint
from faker import Faker
from club.models import Compte
fake = Faker('es_ES')

num_comptes = 300

Faker.seed(0)

for _ in range(5):
    print(fake.iban())
