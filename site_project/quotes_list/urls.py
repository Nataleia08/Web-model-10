from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('create-author/', views.create_author, name='create-author'),
    path('create-quote/', views.create_quote, name='create-quote'),
]