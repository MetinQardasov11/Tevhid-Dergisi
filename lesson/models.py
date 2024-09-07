from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='lesson/')
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Sections'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)
        
        

class Topic(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='section/')
    section = models.ForeignKey(Section, related_name='topics', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Topics'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='lessons', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = 'Lessons'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Lesson, self).save(*args, **kwargs)