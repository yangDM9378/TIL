from django.urls import path,include
from . import views
app_name='chattings'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:pk>/',views.detail, name='detail'),
    path('<int:pk>/delete/',views.delete, name='delete'),
]
