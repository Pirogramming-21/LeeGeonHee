from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm

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


