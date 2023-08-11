from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail, name='post_detail'),
    path('create_post/',views.create_post, name='create'),
    path('update_post/<int:pk>/',views.update_post, name='update_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('search/', views.search, name="search"),
    path('category/<slug:category_slug>/', views.category_view, name="category_view"),
]