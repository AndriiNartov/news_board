from celery import shared_task

from .models import Post


@shared_task
def reset_post_upvotes():
    Post.upvotes_amount.through.objects.all().delete()
    return "Upvotes count was successfully reset"
