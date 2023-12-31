from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('password', views.change_password, name='change_password'),
    path('info', views.user_info, name='user_info'),
]
