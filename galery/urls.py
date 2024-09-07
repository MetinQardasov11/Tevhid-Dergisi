from django.urls import path
from . import views

app_name = 'galery'

urlpatterns = [
    path('', views.index, name='galery'),
]