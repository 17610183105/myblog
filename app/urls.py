from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^index_type/(\d+)$',views.index,name='index_type'),
    url(r'^show_article/(\d+)$',views.show_article,name='show_article'),
]
