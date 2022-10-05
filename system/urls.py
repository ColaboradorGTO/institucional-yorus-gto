from django.contrib import admin
from django.urls import path, include 

from django.conf.urls.static import static  
from django.conf import settings  

urlpatterns = [
    path('admin/', admin.site.urls),

    # My urls 
    path('', include('home.urls')), 

    # Ckeditor 
   # path('ckeditor/', include('ckeditor_uploader_urls')),
   path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin 
admin.AdminSite.site_header = 'Institucional Yorus GTO'
admin.AdminSite.site_title = 'Institucional Yorus GTO'
admin.AdminSite.index_title = 'Institucional Yorus GTO'