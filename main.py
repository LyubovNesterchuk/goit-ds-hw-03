from db import collection



# Читання (Read)

# Функція для виведення всіх записів із колекції.
def show_all():
    cats = list(collection.find())
    if not cats:
        print("Котів нема")
    else:
        for cat in cats:
            print(cat)

# Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
def find_cat(name):
    cat = collection.find_one({"name": name})
    print(cat if cat else "Не знайдено")



# Оновлення (Update)

# Функція, яка дозволяє користувачеві оновити вік кота за ім'ям.
def update_age(name, age):
    result = collection.update_one(
        {"name": name},
        {"$set": {"age": age}}
    )
    print("Оновлено" if result.matched_count else "Не знайдено")

# Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям.
def add_feature(name,feature):
    result = collection.update_one(
        {"name": name},
        {"$addToSet": {"features": feature}}
    )
    print("Додано" if result.matched_count else "Не знайдено")



# Видалення (Delete)

# Функція для видалення запису з колекції за ім'ям тварини.
def delete_cat(name):
    result = collection.delete_one({"name": name})
    print("Видалено" if result.deleted_count else "Не знайдено")

# Функція для видалення всіх записів із колекції.
def delete_all():
    result = collection.delete_many({})
    print(f"Видалено {result.deleted_count}")

