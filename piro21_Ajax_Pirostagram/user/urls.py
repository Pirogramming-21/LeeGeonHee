from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


app_name ='user'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search/', views.user_search, name='user_search')
]