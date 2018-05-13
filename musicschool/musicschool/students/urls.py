from django.conf.urls import url
from .import views

urlpatterns = [
 url(r'^$', views.students, name='students'),
]
