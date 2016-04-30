from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Module, Lecture, Notes, Video, Attachment
from django.http import FileResponse
import os
import mimetypes
from wsgiref.util import FileWrapper


def create(request, modulecode, modulepass, lname, password):
    try:
        user = User.objects.get(username=lname)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, user does not exist")
    if Module.objects.filter(module_code=modulecode).exists():
        output = "The module you are trying to create already exists"
        return HttpResponse(output)
    else:
        if user:
            if user.check_password(password) and user.profile.type == "Lecturer":
                module = Module.objects.create(module_code=modulecode,module_password=modulepass, lecturer_name=lname)
                module.save()
                output = "Success, the module called %s was created" % (
                    module.module_code
                )
                return HttpResponse(output)
            else:
                return HttpResponse("Failure, Password incorrect or user is not a lecturer")


def add_lecture(request, modulecode, lname, password):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, Module does not exist")
    try:
        user = User.objects.get(username=lname)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, user does not exist")
    if module:
        if user:
            if user.check_password(password) and user.profile.type == "Lecturer":
                module.lecture_num = (module.lecture_num + 1)
                module.save()
                lecture = Lecture.objects.create(modulecode=module, lecture_num=module.lecture_num)
                lecture.save()
                output = "Success, the lecture: %s has successfully been created" % (
                    lecture.lecture_num
                )
                return HttpResponse(output)
            else:
                return HttpResponse("Failure, user password incorrect or user is not a lecturer")


def add_notes(request,modulecode,lecturenum,lname,password,notesname):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to add notes to does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module,lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to add notes to does not exist")
    try:
        user = User.objects.get(username=lname)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the user does not exist")
    if lecture:
        if user.check_password(password) and user.profile.type == "Lecturer":
            lecture.notes_num = (lecture.notes_num + 1)
            lecture.save()
            notes = Notes.objects.create(lecture_name=lecture, notes_name=notesname, notes=request.FILES['notes'],notes_num=lecture.notes_num)
            notes.save()
            output = "Success, notes named %s with path %s have successfully been added" % (
                notes.notes_name, notes.notes.path
            )
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, user password incorrect or user is not a lecturer")


def add_video(request,modulecode,lecturenum,lname,password):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to add video to does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to add video to does not exist")
    try:
        user = User.objects.get(username=lname)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the user does not exist")
    if lecture:
        if user.check_password(password) and user.profile.type == "Lecturer":
            lecture.video_num = (lecture.video_num + 1)
            lecture.save()
            video = Video.objects.create(lecture=lecture,  video=request.FILES['video'], video_num=lecture.video_num)
            video.save()
            output = "Success, the video called %s has been created" % (
                video.video.name
            )
            return HttpResponse(output)
        else:
            output = "Failure, Password incorrect or user is not a lecturer"
            return HttpResponse(output)


def add_attachment(request, modulecode, lecturenum, lname, password, attachmentname):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to add attachments to does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to add attachments to does not exist")
    try:
        user = User.objects.get(username=lname)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the user does not exist")
    if lecture:
        if user.check_password(password) and user.profile.type == "Lecturer":
            lecture.attachment_num = (lecture.attachment_num + 1)
            lecture.save()
            attachments = Attachment.objects.create(lecture=lecture,  attachment_name=attachmentname,
                                                    attachment=request.FILES['attachment'],
                                                    attachment_num=lecture.attachment_num)
            attachments.save()
            output = "Success, the attachment named %s was added." % (
                attachments.attachment_name
            )
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, user password incorrect or user is not a lecturer")


def get_lecture_count(request,modulecode):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you requested does not exist")
    if module:
        output = module.lecture_num
        return HttpResponse(output)


def get_notes_count(request,modulecode,lecturenum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you requested does not exist")
    if module:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
        if lecture:
            output = lecture.notes_num
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, could not find lecture with given number")


def get_videos_count(request,modulecode,lecturenum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you requested does not exist")
    if module:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
        if lecture:
            output = lecture.video_num
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, could not find lecture with given number")


def get_attachments_count(request,modulecode,lecturenum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you requested does not exist")
    if module:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
        if lecture:
            output = lecture.attachment_num
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, could not find lecture with given number")


def get_notes(request,modulecode,lecturenum,notesnum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to get notes from does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to get notes from does not exist")
    try:
        note = Notes.objects.get(lecture_name=lecture, notes_num=notesnum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the notes you are trying to get do not exist")
    if note:
        response = HttpResponse(FileWrapper(file(note.notes.path, 'rb')),
                                content_type=mimetypes.guess_type(note.notes.path)[0])
        response['Content-Disposition'] = 'attachment; filename=%s' % note.notes_name
        return response
    else:
        HttpResponse("Failure, could not find notes")


def get_video(request,modulecode,lecturenum,videonum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to get video from does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to get video from does not exist")
    video = Video.objects.get(lecture=lecture, video_num=videonum)
    if video:
        wrapper = FileWrapper(file(video.video.path, 'rb'))
        content_type = mimetypes.guess_type(video.video.path)[0]
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Length'] = os.path.getsize(video.video.path)
        return response
    else:
        HttpResponse("Failure, could not find video")


def get_attachment(request,modulecode,lecturenum,attachnum):
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the module you are trying to get attachments from does not exist")
    try:
        lecture = Lecture.objects.get(modulecode=module, lecture_num=lecturenum)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, the lecture you are trying to get attachments from does not exist")
    attachment = Attachment.objects.get(lecture=lecture, attachment_num=attachnum)
    if attachment:
        wrapper = FileWrapper(file(attachment.attachment.path, 'rb'))
        content_type = mimetypes.guess_type(attachment.attachment.path)[0]
        response = HttpResponse(wrapper, content_type=content_type)
        response['Content-Length'] = os.path.getsize(attachment.attachment.path)
        return response
    else:
        HttpResponse("Failure, could not find attachment")
