from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError


client = MongoClient(
    "mongodb+srv://nesterchukl_db_user:5ZAnL4tbO8G6s7oe@cluster0.d0dcu8d.mongodb.net/myKittens?retryWrites=true&w=majority",
    server_api=ServerApi('1')
)

db = client["myKittens"]
collection = db["kittens"]

# Створення документів (Сreate)

# Функція для заповнення початковими даними
def seed_data():
    
    try:
        collection.delete_many({})

        collection.insert_many(
    [
        {
            "name": "Rydik",
            "age": 6,
            "features": ["ходить в капці", "не дає себе гладити", "рудий"],
        },
        {
            "name": "Capychina",
            "age": 8,
            "features": ["ходить в капці", "дає себе гладити", "сірий"],
        },
        {
            "name": "Sonya",
            "age": 12,
            "features": ["ходить в лоток", "дає себе гладити", "рудий"],
        },
        {
            "name": "Sergiyko",
            "age": 12,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
    ]
)
        print("Дані додано")
    except PyMongoError as e:
        print(f"Помилка: {e}")

seed_data()
