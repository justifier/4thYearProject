from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^create_user%type=(?P<type>[\w]+)%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)'
        r'%code=(?P<activation>[\w]+)$', views.create_user, name='create_user'),
    url(r'^add_module%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)%module=(?P<modulecode>[\w]+)'
        r'%code=(?P<activationcode>[\w]+)', views.add_module, name='add_module'),
    url(r'^delete_module%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)%module=(?P<modulecode>[\w]+)',
        views.delete_module, name='delete_module'),
    url(r'^login%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)', views.login, name='add_module'),
]
