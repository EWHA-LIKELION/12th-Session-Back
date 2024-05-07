from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField('Title', max_length=50, blank=True)
    upload_time = models.DateTimeField(unique=True)
    content = models.TextField('Content')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    
class Comment(models.Model):
    post=models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def apporve(self):
        self.save()

    def __str__(self):
        return self.comment_text