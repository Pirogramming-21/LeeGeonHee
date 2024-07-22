from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name ='board'

urlpatterns = [
    path('board/list', views.board_list, name='board_list'),
    path('board/create', views.board_create, name='board_create'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('board/detail/<int:pk>', views.board_detail, name='board_detail'),
    path('', views.board_feed, name='board_feed'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)