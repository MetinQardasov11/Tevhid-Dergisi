from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory
from django.db.models import Count
from lesson.models import Lesson
from html import unescape
from re import split

def extract_first_n_sentences(text, n=3):
    text = unescape(text)
    sentences = split(r'(?<=[.!?]) +', text)
    return ' '.join(sentences[:n])


def index(request):
    articles = Article.objects.all()
    return render(request, 'article/article.html', {'articles': articles})


def category(request, slug):
    category = get_object_or_404(ArticleCategory, slug=slug)
    articles = Article.objects.filter(category=category)
    return render(request, 'article/category.html', {'category': category, 'articles': articles})


def article_detail(request, category_slug, article_slug):
    articles = Article.objects.select_related('category').order_by('-date')[:3]
    article = get_object_or_404(Article, slug=article_slug, category__slug=category_slug)
    categories = ArticleCategory.objects.annotate(article_count=Count('articles'))
    category = article.category
    summary = extract_first_n_sentences(article.text, n=3)
    lessons = Lesson.objects.filter(is_active=True).select_related('topic__section').order_by('-created_at')[:5]
    context = {
        'article': article,
        'articles': articles,
        'categories': categories,
        'summary': summary,
        'category': category,
        'lessons': lessons
    }
    return render(request, 'article/article_detail.html', context)