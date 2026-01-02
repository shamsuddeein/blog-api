# posts/views.py
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
# from django.shortcuts import render
# from rest_framework import generics, permissions

from .permissions import IsAuthorOrReadOnly #new
from .models import Post
from .serializers import PostSerializer, UserSerializer

# class PostList(generics.ListCreateAPIView):
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly,] # Any user can see the list, only authenticated users can create posts
#     permission_classes = [IsAuthorOrReadOnly,] #new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = [permissions.IsAdminUser,] # Only admin users can update or delete posts
#     permission_classes = [IsAuthorOrReadOnly,] #new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,] #new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser,]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer