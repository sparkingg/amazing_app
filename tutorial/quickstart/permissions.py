from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticatedOrReadOnly


class IsTweetAuthorOrReadOnly(IsAuthenticatedOrReadOnly):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, tweet):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            request.user and
            request.user.is_authenticated and
            tweet.author == request.user
        )