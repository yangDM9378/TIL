# 프레임워크 기반 웹 페이지 구현

## Model
### 모델 생성 및 구축
```
class Movie(models.Model):
    title=models.CharField(max_length=20)
    audience=models.IntegerField()
    release_date=models.DateField()
    genre=models.CharField(max_length=30)
    score=models.FloatField()
    poster_url=models.TextField()
    description=models.TextField()

```
- 데이터 유형/모델 명령어
    - varchar->CharField
    - interger->IntegerField
    - float->FloatField
    - date->DateField
    - text->TextField

## URL
### urls.py
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]
```
- include를 활용하여 movies폴더 내의 urls.py와 연결

### movies/urls.py
```
from django.urls import path,include
from . import views
app_name='movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),    
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```
- import . import views로 views.py와 연결

## Views
### index
- model에서 가져온 데이터를 추출하여 index.html로 이동

### new
- new html로 연결

### create
- 데이터를 POST하여 Movie의 모델에 저장

### detail
- pk(기본키)를 통해 Movie모델에서 movie값 추출

### edit
- pk(기본키)를 통해 edit.html에 필요한 데이터 추출

### update
- Movie모델에 데이터값을 가져오기

### delete
- 삭제한 데이터 값 가져오기

## Admin 등록
```
from django.contrib import admin
from .models import Movie
admin.site.register(Movie)
```
- admin site등록
- admin site에서 데이터 생성, 조회, 수정, 삭제 가능

## templates
### base.html
- 상속받을 파일 html기본 body에 block을 통해 상속

### index.html
```
{% for movie in movies %}
    <a href={% url "movies:detail" movie.pk %}> {{ movie.title }} </a>
    <p>{{ movie.score }}</p>
{% endfor %}
```
- 가져온 movies 데이터를 {{for}}을 통해 만들기

### detail.html
```
<a href="{% url 'movies:edit' movie.pk %}">EDIT</a><br>

```
- {% url %}을 통해 경로 연결

### new.html
```
    <form action="{% url 'movies:create' %}" method="POST" id="new">
```
- method="POST"를 통해 데이터 값 보내기

