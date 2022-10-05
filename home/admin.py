from django.contrib import admin

from . models import Category, Blog, Collection

# Register your models here.

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Collection)