from rest_framework import serializers
from blog.models import Post, LANGUAGE_CHOICES
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'comment_text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'date', 'body', 'language', 'comments']
    '''
    위에랑 똑같은 의미임
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True, max_length = 200)
    date = serializers.DateTimeField('date published')
    body = models.TextField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 1)
    '''
