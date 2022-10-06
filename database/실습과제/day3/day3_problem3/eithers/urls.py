from django.contrib import admin
from django.urls import path,include
from . import views


app_name='eithers'
urlpatterns = [
    path('',views.index, name='index'),
    path('create/', views.create, name='create'),
    path('random/', views.random2, name='random2'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comment/',views.comments_create, name='comments_create'),
]
