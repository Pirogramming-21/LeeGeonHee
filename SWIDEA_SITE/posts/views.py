from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Case, When, BooleanField
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def main(request):
    sort_option = request.GET.get('sort', 'created')
    if sort_option == 'likes':
        posts = Post.objects.all().order_by('-interest', '-created_at')
    elif sort_option == 'name':
        posts = Post.objects.all().order_by('title')
    elif sort_option == 'updated':
        posts = Post.objects.all().order_by('-updated_at')
    else:  # 'created' or default
        posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 8)  # 한 페이지당 8개의 아이디어
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'posts': page_obj,
        'page_obj': page_obj,
        'sort_option': sort_option
    }
    return render(request, 'posts/list.html', ctx)
def create(req):
    if req.method == 'GET':
        form = PostForm()
        ctx = {'form':form}
        return render(req, 'posts/create.html', ctx)
    form = PostForm(req.POST, req.FILES)
    if form.is_valid():
        post = form.save(commit=False)  
        post.user = req.user
        post.save()
    return redirect('posts:main')

def detail(req, pk):
    post = Post.objects.select_related('devtool').get(id=pk)
    ctx = {'post':post, 'pk':pk}
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

def post_list(req):   
    sort_option = req.GET.get('sort', 'created')  
    if sort_option == 'likes':
        ideas = Post.objects.annotate(
            is_starred=Case(
                When(starred=True, then=True),
                default=False,
                output_field=BooleanField()
            )
        ).order_by('-is_starred', 'created_at')
    elif sort_option == 'name':
        ideas = Post.objects.all().order_by('name')  
    elif sort_option == 'updated':
        ideas = Post.objects.all().order_by('-updated_at')  
    else:
        ideas = Post.objects.all().order_by('created_at')  

    paginator = Paginator(ideas, 4)  # 한 페이지당 4개의 아이디어
    page_number = req.GET.get('page')
    page_obj = paginator.get_page(page_number)

    ctx = {
        'ideas': page_obj,
        'page_obj': page_obj,
        'sort_option': sort_option
    }

    return render(req, 'posts/list.html', ctx)



@require_POST
@csrf_exempt
def update_interest(request, pk, action):
    try:
        post = Post.objects.get(pk=pk)
        if action == 'increase':
            post.interest += 1
        elif action == 'decrease':
            post.interest = max(0, post.interest - 1)
        post.save()
        return JsonResponse({'success': True, 'new_interest': post.interest})
    except Post.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Post not found'}, status=404)