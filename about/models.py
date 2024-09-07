from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'