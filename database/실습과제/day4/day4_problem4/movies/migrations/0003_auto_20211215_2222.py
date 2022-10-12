# Generated by Django 3.2.7 on 2021-12-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_like_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='movies.Hashtag'),
        ),
    ]
