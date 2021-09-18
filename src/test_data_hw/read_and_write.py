from csv import DictReader
from collections import OrderedDict
import json

with open('./test_files/books.csv', newline='') as f:
    books = DictReader(f)

    books_list = []

    for book in books:
        books_list.append(book)

with open('./test_files/users.json', 'r') as f:
    users = json.loads(f.read())

i = 0

while i < len(books_list):
    for user in users:
        if i == len(books_list):
            break
        elif 'books' in user:
            user['books'].append(books_list[i])
        else:
            user['books'] = [books_list[i]]
        i += 1

for user in users:
    keys_to_save = ["name", "gender", "address", "age", "books"]
    for key, value in list(user.items()):
        if key not in keys_to_save:
            del user[key]
        else:
            continue

ordered_users = []

for user in users:
    ordered_user = OrderedDict(list(user.items()))
    ordered_user.move_to_end("age")
    ordered_user.move_to_end("books")
    ordered_users.append(ordered_user)

with open('./test_files/result.json', 'w') as f:
    readers = json.dumps(ordered_users, indent=4)
    f.write(readers)
