 
1.
article=Article()
article.title='제목'
article.content='내용'
article.save()

article=Article(title='제목',content='내용')
article.save()

Article.objects.create(title='제목',content='내용')

2.
python manage.py makemigrations
python manage.py migrate