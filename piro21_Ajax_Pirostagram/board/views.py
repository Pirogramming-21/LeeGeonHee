from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
def board_list(req):
    boards = Board.objects.all()
    ctx = {
        'boards' : boards
    }
    return render(req, 'board/list.html', ctx)

def board_create(req):
    if req.method =='POST':
        form = BoardForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
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



