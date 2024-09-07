from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.index, name='article'),
    path('<slug:slug>/', views.category, name='category'),
    path('<slug:category_slug>/<slug:article_slug>/', views.article_detail, name='article_detail'),
]