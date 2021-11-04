from rest_framework import serializers

from .models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    upvotes_amount = serializers.IntegerField(
        source="upvotes_amount.count", read_only=True
    )
    author_name = serializers.CharField(source="author_name.username", read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(PostSerializer):
    pass


class PostDetailSerializer(PostSerializer):
    pass


class PostUpdateSerializer(PostSerializer):
    pass


class PostUpvoteSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = ("id", "upvotes_amount")


class PostListSerializer(PostSerializer):
    comments_amount = serializers.IntegerField(source="comments.count")


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author_name.username", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "post_id", "creation_date", "author_name", "content")


class CommentListSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = None
        exclude = ("post",)


class PostCommentListSerializer(PostSerializer):
    comments = CommentListSerializer(many=True)

    class Meta(PostSerializer.Meta):
        fields = ("id", "comments")


class CommentUpdateSerializer(CommentSerializer):
    pass
