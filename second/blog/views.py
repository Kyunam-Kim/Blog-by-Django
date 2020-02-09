from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects # queryset
    return render(request, 'blog/home.html', {'blogs' : blogs})

def result(request):
    return render(request, 'blog/result.html', {})

def title(request):
    return render(request, 'blog/title.html', {})
    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드