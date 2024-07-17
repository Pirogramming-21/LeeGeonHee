from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def main(req):
    posts = Post.objects.all()
    print("Number of posts:", len(posts))
    ctx = {
        'posts' : posts
    }
    return render(req, 'posts/list.html', ctx)

def create(req):
    if req.method == 'GET':
        form = PostForm()
        ctx = {'form':form}
        return render(req, 'posts/create.html', ctx)
    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        form.save()
    return redirect('posts:main')

def detail(req, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post':post}
    return render(req, 'posts/detail.html', ctx)

def delete(req, pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts:main')

def update(req, pk):
    post = Post.objects.get(id=pk)
    if req.method == 'GET':
        form = PostForm(instance=post)
        ctx = {'form':form, 'pk':pk}
        return render(req, 'posts/update.html', ctx)
    form= PostForm(req.POST, req.FILES, instance=post)
    if form.is_valid():
        form.save()
    return redirect('posts:detail',pk)