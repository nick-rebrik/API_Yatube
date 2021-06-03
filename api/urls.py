from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet)
router_v1.register(
    r'v1/posts/(?P<id>\d+)/comments', CommentViewSet, basename='Comment'
)
router_v1.register('v1/group', GroupViewSet)
router_v1.register('v1/follow', FollowViewSet, basename='Follow')

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('', include(router_v1.urls)),
]
