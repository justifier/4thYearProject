from __future__ import unicode_literals
from django.utils.timezone import now
from django.db import models
import os


class Module(models.Model):
    module_code = models.CharField(max_length=64, primary_key=True)
    module_password = models.CharField(max_length=64)
    lecturer_name = models.CharField(max_length=64)
    lecture_num = models.IntegerField(default=0)


class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    modulecode = models.ForeignKey(Module, on_delete=models.CASCADE)
    lecture_date = models.DateField(default=now)
    lecture_num = models.IntegerField(default=99)
    video_num = models.IntegerField(default=0)
    notes_num = models.IntegerField(default=0)
    attachment_num = models.IntegerField(default=0)


class Video(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    video = models.FileField(upload_to=os.path.dirname(__file__)[:-7]+'static/video/%Y/%m/%d')
    video_num = models.IntegerField(default=99)


class Notes(models.Model):
    lecture_name = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    date = models.DateField('Lecture Date', auto_now=True)
    notes_name = models.CharField(max_length=64,default='default')
    notes = models.FileField(upload_to=os.path.dirname(__file__)[:-7]+'static/notes/%Y/%m/%d')
    notes_num = models.IntegerField(default=99)

    def __str__(self):
        return self.notes.name


class Attachment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    attachment_name = models.CharField(max_length=64)
    attachment = models.FileField(upload_to=os.path.dirname(__file__)[:-7]+'static/attachments/%Y/%m/%d')
    attachment_num = models.IntegerField(default=99)
