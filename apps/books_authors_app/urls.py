from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.index2),  
    url(r'^books/(?P<my_val>\d+)$', views.book),
    url(r'^authors/(?P<my_val>\d+)$', views.author),
    url(r'addbook', views.add_book), 
    url(r'addauthor', views.add_author),
    url(r'^addbooktoauthor$', views.addbooktoauthor),
    url(r'^addnewauthor$', views.addnewauthor),
]
