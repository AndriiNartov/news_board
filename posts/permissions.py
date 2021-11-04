from rest_framework import permissions


class PostUpdateDeletePermission(permissions.BasePermission):
    message = "Only author has permission to update or delete post"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.author_name


class CommentUpdateDeletePermission(permissions.BasePermission):
    message = None

    def has_object_permission(self, request, view, obj):
        if request.method in ("POST", "DELETE"):
            self.message = (
                "Only comment author or post author has permission to delete comment"
            )
            return (
                request.user == obj.author_name or request.user == obj.post.author_name
            )
        if request.method in ("POST", "PATCH", "PUT"):
            self.message = "Only author has permission to update comment"
            return request.user == obj.author_name
