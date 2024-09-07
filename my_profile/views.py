from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def profile(request):
    return render(request, 'my_profile/profile.html')

def questions(request):
    return render(request, 'my_profile/questions.html')


def comments(request):
    return render(request, 'my_profile/comments.html')

def results_exam(request):
    return render(request, 'my_profile/results_exam.html')

def update_info(request):
    return render(request, 'my_profile/update_info.html')

def update_password(request):
    return render(request, 'my_profile/update_password.html')

def messages(request):
    return render(request, 'my_profile/messages.html')


def logout(request):
    return HttpResponse('Logout')