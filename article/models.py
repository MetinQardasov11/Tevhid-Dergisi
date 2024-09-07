from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ArticleCategory, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Article Categories"
        

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='article/')
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(ArticleCategory, related_name='articles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Articles"
        
        
