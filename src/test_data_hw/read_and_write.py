from csv import DictReader
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


with open('./test_files/result.json', 'w') as f:
    readers = json.dumps(users, indent=4)
    f.write(readers)
