from django.contrib import admin

# Register your models here.
from .models import Authors, Quotes


admin.site.register(Authors)
admin.site.register(Quotes)
