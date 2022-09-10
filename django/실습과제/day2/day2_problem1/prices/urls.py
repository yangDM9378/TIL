from django.urls import path, include
from . import views

urlpatterns = [
    path('price/<str:thing>/<int:cnt>/', views.price, name='price'),
]
