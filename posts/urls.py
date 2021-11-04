from django.urls import path

from .views import PostCreateView, PostUpvoteView, PostDetailView, PostUpdateView, PostDeleteView, \
    PostCommentCreateView, PostCommentListView, CommentDeleteView, CommentUpdateView, PostListView

urlpatterns = [
    path('', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('<int:pk>/update/', PostUpdateView.as_view()),
    path('<int:pk>/upvote/', PostUpvoteView.as_view()),
    path('<int:pk>/delete/', PostDeleteView.as_view()),
    path('<int:pk>/comments/', PostCommentListView.as_view()),
    path('<int:pk>/comment/create/', PostCommentCreateView.as_view()),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view()),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view())
]
