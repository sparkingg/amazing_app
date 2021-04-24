from django.urls import include, path
from rest_framework_extensions.routers import ExtendedDefaultRouter
from tutorial.quickstart import views
from django.contrib import admin
from tutorial.quickstart.views import UserTweetViewSet

from tutorial.quickstart.router import SwitchDetailRouter

switch_router = SwitchDetailRouter()
router = ExtendedDefaultRouter()
router.register(r'users', views.UserViewSet).register('tweets', UserTweetViewSet, 'user-tweets', ['username'])
router.register(r'users', views.UserViewSet).register('follows', views.FollowsViewSet, 'user-tweets', ['username'])
router.register(r'users', views.UserViewSet).register('followed', views.FollowedViewSet, 'user-tweets', ['username'])
#
# router.register(r'feed', views.FeedViewSet)
switch_router.register(r'follow', views.FollowViewSet)
router.register(r'tweets', views.TweetViewSet)
router.register(r'feed', views.FeedViewSet)
router.register(r'dags', views.DagViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(switch_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]