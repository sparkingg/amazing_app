from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from tutorial.quickstart.serializers import UserSerializer, DagSerializer, TweetSerializer, FollowSerializer, FollowsSerializer, FollowedSerializer
from tutorial.quickstart.models import Dag, Tweet, Follow
from tutorial.quickstart.permissions import IsTweetAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    lookup_field = 'username'


class DagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dag.objects.all()
    serializer_class = DagSerializer


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsTweetAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserTweetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects
    serializer_class = TweetSerializer

    def get_queryset(self):
        return self.queryset.filter(author__username=self.kwargs['parent_lookup_username'])


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet,
                    ):
    queryset = Follow.objects
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            follower=self.request.user,
            follows=User.objects.get(username=self.kwargs[self.lookup_field])
        )

    def get_object(self):
        return self.queryset.filter(
            follower=self.request.user,
            follows__username=self.kwargs[self.lookup_field],
        )


class FeedViewSet(mixins.ListModelMixin,
                  GenericViewSet,):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tweet.objects
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            author__followers__follower=self.request.user
        )
# class FeedViewSet(UserTweetViewSet):
#
#     def get_queryset(self):
#         follows = Follow.objects.filter(follower=self.request.user)
#         follows_list = []
#         for item in follows:
#             follows_list.append(item.follows)
#         # follows = [
#         #     follow.follows for follow
#         #     in Follow.objects.filter(follower=self.request.user)
#         # ]
#         return self.queryset.filter(author__in=follows_list)


class FollowsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowsSerializer

    def get_queryset(self):
        return self.queryset.filter(follower__username=self.kwargs['parent_lookup_username'])
#
#
class FollowedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowedSerializer

    def get_queryset(self):
        return self.queryset.filter(follows__username=self.kwargs['parent_lookup_username'])


# class FeedViewSet(TweetViewSet):
#
#     def get_queryset(self):
#         Follow.objects.filter(follower=self.request.user)
#
#         return self.queryset.filter(author__username=Follow.follows)




