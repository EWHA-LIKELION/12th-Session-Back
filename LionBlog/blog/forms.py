from dataclasses import field
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['username', 'comment_text']