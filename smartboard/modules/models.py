from __future__ import unicode_literals

from django.db import models


class Lecture(models.Model):
    module_code = models.CharField(max_length=64)
    lecturer_name = models.CharField(max_length=64)


class Video(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    video = models.FileField(upload_to='/media/videos')


class Notes(models.Model):
    lecture_name = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    date = models.DateField('Lecture Date', auto_now=True)
    notes_name = models.CharField(max_length=64,default='default')
    notes = models.FileField(upload_to='/College/4thYearProject/smartboard/media/notes')

    def __str__(self):
        return self.notes.name

class Attachment(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    attachment_name = models.CharField(max_length=64)
    attachment = models.FileField(upload_to='/media/attachments')
