from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shop_list, name='shop_list'),
    url(r'^(?P<pk>\d+)/new/$', views.order, name='order'),
]
