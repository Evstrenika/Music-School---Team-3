from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
 url(r'^$', views.home),
 url(r'^login/$', login, {'template_name': 'pages/login.html'}),
 url(r'^logout/$', logout, {'template_name': 'pages/logout.html'}),
 url(r'^application/$', views.application, name='application'),
]