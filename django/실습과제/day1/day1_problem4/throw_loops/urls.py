from django.urls import path, include
from . import views

app_name='throw_loops'
urlpatterns = [
    path('first/', views.first, name='first'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),

]
