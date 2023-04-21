from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
]