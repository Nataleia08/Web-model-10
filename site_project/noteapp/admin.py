from django.contrib import admin

# Register your models here.
from .models import Authors, Quotes, UsersSite

admin.site.register(Authors)
admin.site.register(Quotes)
admin.site.register(UsersSite)