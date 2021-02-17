from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include


router = DefaultRouter()

router.register(r"posts", views.PostViewSet, basename="post")
router.register(r"posts/(?P<post_id>\d+)/comments", views.CommentViewSet, basename="comment")
router.register(r"follow", views.FollowView, basename="follow")
router.register(r"group", views.GroupView, basename="group")

urlpatterns = [
    path("v1/", include(router.urls))
]
