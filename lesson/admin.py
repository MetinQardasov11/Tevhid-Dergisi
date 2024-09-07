from django.contrib import admin
from .models import Lesson, Section, Topic
from django.utils.safestring import mark_safe


# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    readonly_fields = ['slug']


class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'section', 'slug']
    search_fields = ['name']
    readonly_fields = ['slug']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'topic', 'slug']
    search_fields = ['name']
    readonly_fields = ['slug']
    


admin.site.register(Section, SectionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Lesson, LessonAdmin)