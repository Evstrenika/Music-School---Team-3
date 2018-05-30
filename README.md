# Team-3

************************LOGIN DETAILS*******************************

Admin Gmail Login: 
Username: testdevelopmentuser1@gmail.com
Password: lhb2a7L7m2hFjdLKLxYy

Admin Login:
UN: veronika
PW: ifb299qut

UN: Owner (super user)
PW: ifb299qut

Student Login:
UN: student1
PW: password.1

UN: teststudent1
PW: jQiAWGEod2h5xqgcul2I

UN: teststudent2
PW: t90j5cbfrTYQP1JSvTXM

Teacher Login:
UN: teacher2
PW: password.3

UN: testteacher1
PW: 8eP8ykb2oteeOgGMYbGN


*********************INSTRUCTIONS***********************************

# install visual studio 2015, try to create a python django project it will ask to install
python tools, create project as python 3.5 in virtual environment
# install posgres, use default settings for user, port, whatever password
# create musicschool db in postgres
# create project in visual studio Python > Web > Blank Django make a virtual env
for python 3.5
# settings.py in visual studio
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'musicschool',
        'USER': 'postgres',
        'PASSWORD': '1234' OR ‘secret’ (try both and see which one works), 
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}
# add sites (just remove if there's some admin error)
INSTALLED_APPS = [
    # Add your apps here to enable them
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
]
# open cmd (command line) navigate to virtual environment created by visual studio (env) Scripts folder e.g
C:\Users\owner\Documents\Visual Studio 2015\ifb299\musicschool\musicschool\env\Scripts. then type "activate" 
# python manage.py createsuperuser, ignore psycog2 error
# pip install psycopg2
# create super user again will cause another authentication error, need to migrate, 
 type python manage.py migrate auth
# type python manage.py migrate 
# python manage.py createsuperuser
user: owner
password: ifb299qut
# in urls.py, from django.conf.urls import include, url
# Uncomment the next two lines to enable the admin,
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', musicschool.views.home, name='home'),
    # url(r'^musicschool/', include('musicschool.musicschool.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
