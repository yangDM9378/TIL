from asyncore import read
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id','title','content',)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    # pk값으로 추가
    # comment_set=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # 모든 댓글 값을 다 보여주게하기
    comment_set=CommentSerializer(many=True, read_only=True)
    comment_count=serializers.IntegerField(source='comment_set.count', read_only=True)
    
    class Meta:
        model = Article
        fields ='__all__'

