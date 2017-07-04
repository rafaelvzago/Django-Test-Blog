# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from core.models import Post
from core.forms import PostForm

# Create your views here.

def home(request):
    return render(request,'core/index.html')

def articles(request):
    articles = Post.objects.all().order_by('-id')
    return render(request,'core/articles.html',{'articles': articles})

def add(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(articles)
    return render(request,'core/add.html', {'form': form})

def update(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect(articles)
    return render(request,'core/add.html', {'form': form})

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect(articles)
