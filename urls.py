# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uploaded/', views.uploaded, name='upload-uploaded'),
    path('execute/', views.executed, name='upload-executed'),
]
