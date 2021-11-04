from django.contrib import admin

from .models import Comment, Post, User


admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(User)
