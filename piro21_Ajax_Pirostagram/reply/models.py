from django.db import models
from django.contrib.auth.models import User
from board.models import Board
# Create your models here.
class Reply(models.Model):
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content