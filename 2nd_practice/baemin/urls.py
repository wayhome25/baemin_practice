from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^(?P<shop_id>\d+)/new/$', views.order_new, name='order_new'),
]
