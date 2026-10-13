import json
from csv import reader


# Читаем json из файла users.json
with open("users.json", "r") as file:
    data1 = json.load(file)

# Берем нужную часть и добавляем информацию
processed_users = []
for user in data1:
    # Берем только нужные поля
    new_user = {
        "name": user["name"],
        "gender": user["gender"],
        "address": user["address"],
        "age": user["age"]
    }
    processed_users.append(new_user)

print(100 * "=")
print(processed_users)
print(100 * "=")

with open("result.json", "w") as file:
    json.dump(processed_users, file)


# Читаем csv из файла books.csv
with open("books.csv", newline='') as file:
    reader = reader(file)

    header = next(reader)

    for row in reader:
        # print(row)
        print(dict(zip(header, row)))
