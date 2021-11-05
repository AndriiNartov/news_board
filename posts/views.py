from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListAPIView,
    get_object_or_404,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated


from .models import Comment, Post
from .serializers import (
    PostCreateSerializer,
    PostUpdateSerializer,
    PostUpvoteSerializer,
    CommentSerializer,
    PostCommentListSerializer,
    PostDetailSerializer,
    CommentUpdateSerializer,
    PostListSerializer,
)
from .permissions import CommentUpdateDeletePermission, PostUpdateDeletePermission


class PostCreateView(CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)


class PostDetailView(RetrieveAPIView):
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostUpdateView(UpdateAPIView):
    serializer_class = PostUpdateSerializer
    queryset = Post.objects.all()
    http_method_names = ["patch"]
    permission_classes = [PostUpdateDeletePermission]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(
                {"message": "failed", "details": serializer.errors}, status=400
            )


class PostUpvoteView(UpdateAPIView):
    serializer_class = PostUpvoteSerializer
    queryset = Post.objects.all()
    http_method_names = ["patch"]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user not in post.upvotes_amount.all():
            post.upvotes_amount.add(request.user)
            post.save()
            return Response(data=self.get_serializer(post).data)
        return Response(
            {
                "message": "failed",
                "details": f"User {request.user.username} is already upvoated this post",
            },
            status=400,
        )


class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [PostUpdateDeletePermission]


class PostListView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]


class PostCommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        author_name = self.request.user
        serializer.save(post=post, author_name=author_name)


class CommentUpdateView(PostUpdateView):
    serializer_class = CommentUpdateSerializer
    queryset = Comment.objects.all()
    permission_classes = [CommentUpdateDeletePermission]


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [CommentUpdateDeletePermission]


class PostCommentListView(PostDetailView):
    serializer_class = PostCommentListSerializer
    permission_classes = [AllowAny]
