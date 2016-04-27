from django.conf.urls import url

from . import views

app_name = 'modules'
urlpatterns = [
    url(r'^create%module=(?P<module>[\w]+)%lecture=(?P<lname>[\w]+)%password=(?P<password>[\w]+)$',
        views.create, name='create_module'),
    url(r'^add_notes%module=(?P<module>[\w]+)%lecture=(?P<lname>[\w]+)%password=(?P<password>[\w]+)'
        r'%notes=(?P<notesname>[\w]+)$', views.add_notes, name='add_notes'),
    url(r'^get_notes%module=(?P<module>[\w]+)$', views.get_notes, name='get_notes'),
]