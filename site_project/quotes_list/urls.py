from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('create-author/', views.signupuser, name='create-author'),
]