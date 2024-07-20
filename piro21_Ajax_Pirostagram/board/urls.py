from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name ='board'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('board/create', views.board_create, name='board_create')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)