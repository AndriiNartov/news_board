from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    link = models.URLField(verbose_name='Link')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')
    upvotes_amount = models.ManyToManyField(User, blank=True, null=True, verbose_name='Upvotes amount')
    author_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='posts',
        blank=True,
        null=True
    )


class Comment(models.Model):
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author', related_name='comments')
    content = models.TextField(verbose_name='Content')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Creation date')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Post')
