from django.contrib.auth.models import User
from rest_framework import serializers
from tutorial.quickstart.models import Dag, Tweet, Follow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'last_name', 'first_name']
        extra_kwargs = {'url': {'lookup_field': 'username'}}


class DagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dag
        fields = ['url', 'name', 'owner']


class TweetSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ['id', 'text', 'photo', 'created', 'author']


class FollowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Follow
        fields = []


class FollowsSerializer(serializers.HyperlinkedModelSerializer):
    follows = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['follows', 'followed']


class FollowedSerializer(serializers.HyperlinkedModelSerializer):
    follower = UserSerializer(read_only=True)

    class Meta:
        model = Follow
        fields = ['follower', 'followed']




