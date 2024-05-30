from rest_framework import serializers
from .models import Post, Comment
from api.models import User

# class Post(models.Model):
#     title=models.CharField(max_length=200)
#     date=models.DateTimeField('date published')
#     body = models.TextField()
#     language = models.IntegerField(choices = LANGUAGE_CHOICES)

#     def __str__ (self):
#         return self.title
    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     username = models.CharField(max_length=20)
#     comment_text=models.TextField()
#     created_at=models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.comment_text


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','username','comment_text','created_at']


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Post
        fields = ['id','title', 'date', 'body', 'lanuage', 'comments']

    '''
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(required = False, allow_blank = True, max_length = 200)
    date = serializers.DateTimeField('date published')
    body = models.TextField()
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 1)
    '''


