from django.shortcuts import render, get_object_or_404
from .models import Lesson, Section, Topic
from article.models import Article

# Create your views here.

def section_page(request):
    sections = Section.objects.filter(is_active=True)
    context = {
        'sections': sections
    }
    return render(request, 'lesson/section.html', context)

def topic_page(request, section_slug):
    section = get_object_or_404(Section, slug=section_slug)
    topics = Topic.objects.filter(section=section, is_active=True)
    context = {
        'section': section,
        'topics': topics
    }
    return render(request, 'lesson/topic.html', context)


def lesson_page(request, section_slug, topic_slug):
    section = get_object_or_404(Section, slug=section_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, section=section)
    lessons = Lesson.objects.filter(topic=topic, is_active=True)
    articles = Article.objects.select_related('category').order_by('-date')[:3]
    lessons_five = Lesson.objects.filter(is_active=True).select_related('topic__section').order_by('-created_at')[:5]
    context = {
        'section': section,
        'topic': topic, 
        'lessons': lessons,
        'articles': articles,
        'lessons_five': lessons_five
    }
    return render(request, 'lesson/lesson.html', context)

def lesson_detail(request, section_slug, topic_slug, lesson_slug):
    section = get_object_or_404(Section, slug=section_slug)
    topic = get_object_or_404(Topic, slug=topic_slug, section=section)
    lessons = get_object_or_404(Lesson, slug=lesson_slug, topic=topic)
    # get the lesson when I clikc this
    lesson = Lesson.objects.get(slug=lesson_slug, topic=topic)
    context = {
        'section': section,
        'topic': topic,
        'lessons': lessons,
        'lesson': lesson
    }
    return render(request, 'lesson/lesson_detail.html', context)