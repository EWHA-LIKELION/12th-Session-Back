from django.contrib import admin

# Register your models here.
from blog.models import *

# Register your models here.
admin.site.register(Post)

admin.site.register(Comment)
