from django.urls import path

# My views 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.about, name='sobre'),
    path('blog/', views.blog, name='blog'),
    path('detalhes-do-blog/<slug:slug>/', views.blog_detail, name='detalhes-do-blog'), 
    path('contato', views.contact, name='contato'), 
]



