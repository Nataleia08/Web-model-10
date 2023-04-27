from pymongo import MongoClient
import json
from datetime import datetime

client = MongoClient("mongodb+srv://nataleia_orlovska:uj40A6wY74dc4u@clusterhw7.uaenqgk.mongodb.net/?retryWrites=true&w=majority")
db = client.Home_Work_7


authors = db.authors.find()
list_authors = []

for author in authors:
    new_author = {}
    new_author["fullname"] = str(author["fullname"])
    new_author["born_date"] = str(author["born_date"].date())
    new_author["born_location"] = str(author["born_location"])
    new_author["description"] = str(author["description"])
    list_authors.append(new_author)

with open("authors.json", "w") as fh:
    json.dump(list_authors, fh, indent=6)

quotes = db.quotes.find()
quotes_list = []

for quote in quotes:
    new_quote = {}
    new_quote["quote"] = str(quote['quote'])
    new_quote["tags"] = str(quote["tags"])
    au = db.authors.find_one({"_id": quote['author']})
    if au:
        new_quote["author"] = str(au["fullname"])
        quotes_list.append(new_quote)


with open("quotes.json", "w") as fh:
    json.dump(quotes_list, fh, indent=6)


user_list_object = list(db.contact.find())
user_list = []

for us in user_list_object:
    new_user = {}
    new_user["nickname"] = str(us["fullname"])
    new_user["email"] = str(us["email"])
    new_user["phone"] = str(us["phone"])
    new_user["login"]= str(us["email"])
    user_list.append(new_user)

with open("user_list.json", "w") as fh:
    json.dump(user_list, fh, indent=6)