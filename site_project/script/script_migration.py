import os
import django
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "site_project.settings")
django.setup()


from pymongo import MongoClient

client = MongoClient("mongodb+srv://nataleia_orlovska:uj40A6wY74dc4u@clusterhw7.uaenqgk.mongodb.net/?retryWrites=true&w=majority")
db = client.Home_Work_7




authors = db.authors.find()

for author in authors:
    Authors.objects.get_or_create(fullname = author["fullname"], born_date = author["born_date"],
                                  born_location = author["born_location"], description = author["description"])

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name = tag)
        tags.append(t)
    exist_quote = bool(len(Quotes.objects.filter(quote=quote["quote"])))

    if not exist_quote:
        author = db.authors.find_one({"_id": quote['author']})
        au = Authors.objects.get(fullname = author["fullname"])
        qu = Quotes.objects.create(quote = quote['quote'], author = au)
        for tag in tags:
            qu.tags.add(tag)

user_list = db.contact.find()

for us in user_list:
    UsersSite.objects.get_or_create(nickname = us["fullname"], email = us["email"],
                                    phone=us["phone"] , login= us["email"])
