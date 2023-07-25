from django.urls import path
from . import views

urlpatterns = [
    path('update_comment/<int:postpk>/<int:commentpk>/',views.update_comment, name='update_comment'),
    path('delete_comment/<int:postpk>/<int:commentpk>/',views.delete_comment, name='delete_comment'),
]