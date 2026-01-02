# posts/views.py
from django.shortcuts import render
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly #new
from .models import Post
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,] # Any user can see the list, only authenticated users can create posts
    permission_classes = [IsAuthorOrReadOnly,] #new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAdminUser,] # Only admin users can update or delete posts
    permission_classes = [IsAuthorOrReadOnly,] #new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


