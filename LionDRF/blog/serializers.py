from rest_framework import serializers
from blog.models import *
from api.models import *

#  '''
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required = False, allow_blank = True, max_length = 200)
#     date = serializers.DateTimeField('date published')
#     body = models.TextField()
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default = 1)
#     '''

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'username', 'comment_text', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'date', 'body', 'language', 'comments']



# class UserSerializer(serializer.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']

#     def create(self, validated_data):
#         user = User.objects.create(
#             email=validated_data['email'],
#             username=validated_data['username'],
#         )
#         user.set_password(validated_data['password'])
#         user.save()

#         return user