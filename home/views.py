from django.shortcuts import render, get_object_or_404
from home.models import Post

def two_buttons(request):
    return render(request, 'home.html')

def cv_view(request):
    return render(request, 'CVs.html')

def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html', {'posts': posts})

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})