from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('page/<int:page>', views.main, name = "root_paginator"),
    path('create-author/', views.create_author, name='create_author'),
    path('create-quote/', views.create_quote, name='create_quote'),
    path('detail/<int:author_id>', views.author_details, name='author_details'),
    path('create-tag/', views.tag, name = 'tag'),
    path('tags/<int:tags_id>', views.tags_list, name= 'tags_list'),
    path('script/', views.script, name='script'),
]