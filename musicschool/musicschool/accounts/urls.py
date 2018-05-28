from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
 url(r'^$', views.home),
 url(r'^login/$', login, {'template_name': 'pages/login.html'}),
 url(r'^logout/$', logout, {'template_name': 'pages/logout.html'}),
 url(r'^teacher_application/$', views.Teacher.as_view()),
 url(r'^application/$', views.application, name='application'),
 url(r'^profile/$', views.profile, name='profile'),
 url(r'^profile/edit/$', views.edit, name='edit'),
 url(r'^change_password/$', views.change_password, name='change_password'),
 url(r'^$', views.students, name='students'),
 url(r'^$', views.teachers, name='teachers')

]