from django.conf.urls import url

from . import views

app_name = 'modules'
urlpatterns = [
    url(r'^create%module=(?P<modulecode>[\w]+)%module_password=(?P<modulepass>[\w]+)'
        r'%lecturer=(?P<lname>[\w]+)%password=(?P<password>[\w]+)$', views.create, name='create_module'),
    url(r'^add_lecture%module=(?P<modulecode>[\w]+)%lecturer=(?P<lname>[\w]+)%password=(?P<password>[\w]+)$',
        views.add_lecture, name='add_lecture'),
    url(r'^add_notes%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%lecturer=(?P<lname>[\w]+)'
        r'%password=(?P<password>[\w]+)%notes=(?P<notesname>[\w]+)$', views.add_notes, name='add_notes'),
    url(r'^add_video%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%lecturer=(?P<lname>[\w]+)'
        r'%password=(?P<password>[\w]+)$', views.add_video, name='add_video'),
    url(r'^add_attachment%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%lecturer=(?P<lname>[\w]+)'
        r'%password=(?P<password>[\w]+)%attachment=(?P<attachmentname>[\w]+)$',
        views.add_attachment, name='add_attachment'),
    url(r'^get_notes%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%nnum=(?P<notesnum>[\w]+)$',
        views.get_notes, name='get_notes'),
    url(r'^get_video%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%vnum=(?P<videonum>[\w]+)$',
        views.get_video, name='get_video'),
    url(r'^get_attachment%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)%anum=(?P<attachnum>[\w]+)$',
        views.get_attachment, name='get_attachment'),
    url(r'^get_lecture_count%module=(?P<modulecode>[\w]+)$', views.get_lecture_count, name='get_lecture_count'),
    url(r'^get_notes_count%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)$',
        views.get_notes_count, name='get_notes_count'),
    url(r'^get_videos_count%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)$',
        views.get_videos_count, name='get_videos_count'),
    url(r'^get_attachments_count%module=(?P<modulecode>[\w]+)%lnum=(?P<lecturenum>[\w]+)$',
        views.get_attachments_count, name='get_attachments_count'),
]
