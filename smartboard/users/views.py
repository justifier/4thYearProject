from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from modules.models import Module, Lecture, Video, Attachment, Notes
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
import datetime


def create_user(request, type, name, password, activation):
    if type == "Student":
        try:
            user = User.objects.create_user(
                username=name,
                password=password
            )
        except IntegrityError as e:
            return HttpResponse("Failure, user with that id already exists")
        student = user.profile
        student.save()
    else:
        if type == "Lecturer":
            if activation == "test":
                try:
                    user = User.objects.create_user(
                        username=name,
                        password=password
                    )
                except IntegrityError as e:
                    return HttpResponse("Failure, user with that id already exists")
                lecturer = user.profile
                lecturer.type = 'Lecturer'
                lecturer.save()
            else:
                return HttpResponse("Failure,invalid activation code.")
    return HttpResponse("Success, The user was successfully created.")


def add_module(request, name, password, modulecode, activationcode):
    user = User.objects.get(username=name)
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, module does not exist")
    if user.check_password(password):
        if activationcode == "test":
            if module is not None:
                profile = user.profile
                if profile.modules:
                    if modulecode in profile.modules:
                        return HttpResponse("Failure, module already attached to user")
                    else:
                        profile.modules = (profile.modules + ',' + modulecode)
                else:
                    profile.modules = modulecode
                profile.save()
                output = "Success, the module: %s has been added to user %s" % (
                    user.username, user.profile.modules
                )
                return HttpResponse(output)
    return HttpResponse("Failure, password was incorrect")


def delete_module(request, name, password, modulecode):
    try:
        user = User.objects.get(username=name)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, user does not exist")
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, module does not exist")
    if user.check_password(password):
        if module is not None:
            profile = user.profile
            if profile.modules:
                if "," + modulecode in profile.modules:
                    profile.modules = profile.modules.replace(',' + modulecode, '')
                    profile.save()
                    return HttpResponse("Success,module deleted")
                elif modulecode in profile.modules:
                    profile.modules = profile.modules.replace(modulecode, '')
                    profile.save()
                    return HttpResponse("Success, module deleted")
                else:
                    return HttpResponse("Failure, module was no found in users modules")
    return HttpResponse("Failure, module not deleted")


def login(request, name, password):
    ipadd = "http://192.168.43.243:8000"  ##TODO change ip
    user = User.objects.get(username=name)
    if user.check_password(password):
        if user.profile.type:
            user.last_login = datetime.datetime.now()
            user.save()
            modulelist = user.profile.modules.split(',')
            output = "Name:" + name + "%%%%Password:" + password + "%%%%UserType:" + user.profile.type + "%"
            for x in modulelist:
                output = output + "%%%Module:" + x
                try:
                    tempModule = Module.objects.get(module_code=x)
                except ObjectDoesNotExist:
                    break
                lecturesNo = tempModule.lecture_num
                count = 1
                while count < (lecturesNo + 1):
                    curLecture = Lecture.objects.get(modulecode=x, lecture_num=count)
                    output = output + "%%Lecture:" + str(count)
                    videoNo = curLecture.video_num
                    videocount = 1
                    while videocount < (videoNo + 1):
                        curvid = Video.objects.get(lecture_id=curLecture.lecture_id, video_num=videocount)
                        output = output + "%%Video:" + ipadd + curvid.video.path[36:]
                        videocount += 1
                    notesno = curLecture.notes_num
                    notescount = 1
                    while notescount < (notesno + 1):
                        curnotes = Notes.objects.get(lecture_name_id=curLecture.lecture_id, notes_num=notescount)
                        output = output + "%%Notes:" + ipadd + curnotes.notes.path[36:]
                        notescount += 1
                    attachno = curLecture.attachment_num
                    attachcount = 1
                    while attachcount < (attachno + 1):
                        curAttach = Attachment.objects.get(lecture_id=curLecture.lecture_id, attachment_num=attachcount)
                        output = output + "%%Attachment:" + ipadd + curAttach.attachment.path[36:]
                        attachcount += 1
                    count += 1
            output = output + "%%%%"
            output = output.replace('\\', '/')
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, could not find the user type")
    else:
        output = "Failure, Password incorrect"
        return HttpResponse(output)
