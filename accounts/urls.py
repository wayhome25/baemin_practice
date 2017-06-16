from django.conf.urls import include, url
from django.contrib.auth import views as auth_views # NOTE: 내장 auth view 활용 (login, logout, Password reset)
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login', kwargs = {'template_name': 'accounts/login_form.html'}),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs = {'next_page': 'login'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
]
