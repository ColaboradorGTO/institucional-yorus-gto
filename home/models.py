from django.db import models

# Std image 
from stdimage.models import StdImageField

# Slug na url 
from django.utils.text import slugify 

# Ckeditor 
from ckeditor.fields import RichTextField 

# Create your models here.

class Category(models.Model):
    title = models.CharField('Título', max_length=255)

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'     


class Blog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    title = models.CharField('Título', max_length=255)
    subtitle = models.CharField('Subtítulo', max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = StdImageField('Imagem', upload_to='Blog', variations={'thumb': {'width': 1595, 'height': 824, 'crop': True }})  
    content = RichTextField('Conteúdo', )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog' 

    def save(self, *args, **kwargs):
        value = f'{self.title}, {self.subtitle}, {self.created}' 
        self.slug = slugify(value, allow_unicode=False)    
        super().save(*args, **kwargs)       


class Collection(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = StdImageField('Imagem', upload_to='collection', variations={'thumb': {'width': 1080, 'height': 1350, 'crop': True }})
    title = models.CharField('Título', max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'    



