from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class BlogImages(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    pass

def post_new(request):
    pass

def post_edit(request, pk):
    pass

def js_test(request):
    pass