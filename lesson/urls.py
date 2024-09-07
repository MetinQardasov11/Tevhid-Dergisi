from django.urls import path
from . import views

app_name = 'lesson'

urlpatterns = [
    path('', views.section_page, name='section'),
    path('<slug:section_slug>/', views.topic_page, name='topic'),
    path('<slug:section_slug>/<slug:topic_slug>/', views.lesson_page, name='lessons'),
    path('<slug:section_slug>/<slug:topic_slug>/<slug:lesson_slug>/', views.lesson_detail, name='lesson_detail'),
]