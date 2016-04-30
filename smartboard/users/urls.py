from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^create_user%type=(?P<type>[\w]+)%name=(?P<name>[\w]+)%email=(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.'
        r'[a-zA-Z0-9-.]+)%password=(?P<password>[\w]+)$', views.create_user, name='create_user'),
    url(r'^add_module%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)%module=(?P<modulecode>[\w]+)'
        r'%code=(?P<activationcode>[\w]+)', views.add_module, name='add_module'),
    url(r'^login%name=(?P<name>[\w]+)%password=(?P<password>[\w]+)', views.login, name='add_module'),
]
