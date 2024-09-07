from django.shortcuts import render, get_object_or_404
from article.models import Article, ArticleCategory
from django.db.models import Count
from lesson.models import Section, Topic, Lesson

# Create your views here.

def index(request):
    articles = Article.objects.select_related('category').order_by('-date')[:4]
    lessons = Lesson.objects.filter(is_active=True).select_related('topic__section').order_by('-created_at')[:4]
    context = {
        'articles': articles,
        'lessons': lessons
    }
    return render(request, 'about/about.html', context)