from django.urls import path
from . import views

app_name = 'my_profile'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('sorular/', views.questions, name='questions'),
    path('yorumlar/', views.comments, name='comments'),
    path('test-sonuclari/', views.results_exam, name='results_exam'),
    path('bilgiler/', views.update_info, name='update_info'),
    path('sifre/', views.update_password, name='update_password'),
    path('mesajlar/', views.messages, name='messages'),
    path('logout/', views.logout, name='logout')
]