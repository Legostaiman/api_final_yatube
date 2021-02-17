from .models import (Group,
                     Post,
                     Comment,
                     Follow)
from .serializers import PostSerializer, \
    CommentSerializer, \
    FollowSerializer, \
    GroupSerializer
from .permissions import IsOwnerOrReadOnly


from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


class CustomViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    pass


class GroupView(CustomViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ['group']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        queryset = post.comments.all()
        return queryset


class FollowView(CustomViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']

    def get_queryset(self):
        queryset = Follow.objects.filter(following=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
