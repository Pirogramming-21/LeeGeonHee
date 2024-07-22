from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from reply.forms import ReplyForm

# Create your views here.
def board_list(req):
    boards = Board.objects.all()
    ctx = {
        'boards' : boards,
    }
    return render(req, 'board/list.html', ctx)

@login_required
def board_create(req):
    if req.method =='POST':
        form = BoardForm(req.POST, req.FILES)
        if form.is_valid():
            board = form.save(commit=False)
            board.like=0
            board.save()
            return redirect('board:board_list') 
    else:
        form = BoardForm()

    return render(req, 'board/create.html', {'form': form})

@csrf_exempt
def like_ajax(req):
    req = json.loads(req.body)
    board_id = req['id']

    board = Board.objects.get(id= board_id)
    board.like +=1
    board.save()
    
    return JsonResponse({'id' : board_id})

def board_detail(req,pk):
    board = Board.objects.prefetch_related('reply_set').get(id=pk)
    replyForm = ReplyForm()
    ctx = {
        'board' : board,
        'replyForm' : replyForm,
    }
    return render(req, 'board/detail.html', ctx)

def board_feed(req):
    boards = Board.objects.all()
    ctx = {
        'boards': boards
    }
    return render(req, 'board/feed.html', ctx)



