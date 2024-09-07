from django.db import models
from django.utils.text import slugify

# Create your models here.

class Galery(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='galery/')
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Galery, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Galeries'