from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from modules.models import Module
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
import datetime


def create_user(request,type,name,email,password):
    try:
        user = User.objects.create_user(
            username=name,
            password=password,
            email=email
        )
    except IntegrityError as e:
        return render_to_response("error_response.html", {"message": e})
    if type == "Student":
        student = user.profile
        student.save()
    else:
        if type == "Lecturer":
            lecturer = user.profile
            lecturer.type = 'Lecturer'
            lecturer.save()
    email = User.objects.get(username=name).email
    output = "Success, The user has been created with email: %s " % (
        email
    )
    return HttpResponse(output)


def add_module(request,name,password,modulecode,activationcode):
    user = User.objects.get(username=name)
    try:
        module = Module.objects.get(module_code=modulecode)
    except ObjectDoesNotExist:
        return HttpResponse("Failure, module does not exist")
    if user.check_password(password):
        if activationcode:
            if module is not None:
                profile = user.profile
                if profile.modules:
                    profile.modules = (profile.modules + ',' +modulecode)
                else:
                    profile.modules = module
                profile.save()
                output = "Success, the module: %s has been added to user %s" % (
                    user.username, user.profile.modules
                )
                return HttpResponse(output)
    return HttpResponse("Failure, password was incorrect")


def login(request, name, password):
    user = User.objects.get(username = name)
    if user.check_password(password):
        if user.profile.type:
            user.last_login = datetime.datetime.now()
            user.save()
            output = "Success, The user %s has been logged in with the modules %s, the user type is %s" % (
                name, user.profile.modules, user.profile.type)
            return HttpResponse(output)
        else:
            return HttpResponse("Failure, could not find the user type")
    else:
        output = "Failure, Password incorrect"
        return HttpResponse(output)
