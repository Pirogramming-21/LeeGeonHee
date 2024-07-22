from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name ='reply'

urlpatterns = [
    path('create/<int:pk>', views.reply_create, name='reply_create'),
]
