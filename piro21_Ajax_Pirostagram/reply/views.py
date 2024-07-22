from django.shortcuts import render, redirect
from .models import Board
from django.urls import reverse
from .forms import ReplyForm
from .models import Reply
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

from django.core.serializers import serialize
import json

@login_required
def reply_create(req, pk):
    if req.method == 'POST':
        replyForm = ReplyForm(req.POST)
        if replyForm.is_valid():
            reply = replyForm.save(commit=False)
            reply.writer = req.user
            board = Board.objects.get(id=pk)
            reply.board = board
            reply.save()
            return JsonResponse({'content': reply.contents}, json_dumps_params={'ensure_ascii': False})
    return JsonResponse({'error': 'Invalid request'}, status=400)
