from django.urls import path,include
from . import views

app_name='throw_catch'
urlpatterns = [
    path('throw_catch/first/', views.first, name='first'),
    path('throw_catch/second/', views.second, name='second'),
]
