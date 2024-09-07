from django.shortcuts import render
from article.models import Article, ArticleCategory
from lesson.models import Lesson, Topic
from django.db.models import F

# Create your views here.

def home(request):
    articles = Article.objects.select_related('category').order_by('-date')[:6]
    article_orders = Article.objects.all()
    categories = ArticleCategory.objects.all()
    lessons = Lesson.objects.filter(is_active=True).select_related('topic__section').order_by('-created_at')[:6]
    context =  {
        'articles': articles, 
        'categories': categories,
        'article_orders': article_orders,
        'lessons': lessons
    }
    return render(request, 'home/index.html', context)