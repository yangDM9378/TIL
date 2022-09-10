from django.urls import path, include
from . import views

urlpatterns = [
    path('calculator/<int:first>/<int:second>/', views.calculator, name='calculator')
]
