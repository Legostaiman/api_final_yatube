from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

router = DefaultRouter()

router.register(r"posts", views.PostViewSet, basename="post")
router.register(r"posts/(?P<post_id>\d+)/comments", views.CommentViewSet,
                basename="comment")
router.register(r"follow", views.FollowView, basename="follow")
router.register(r"group", views.GroupView, basename="group")

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
