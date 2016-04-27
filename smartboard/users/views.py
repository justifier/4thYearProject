from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from .models import Student


def create_user(request,type,name,email,password):
    try:
        user = User.objects.create_user(
            username=name,
            password=password,
            email=email
        )
        student = user.student
        student.modules = 'testing'
        user.save()
        student.save()
    except IntegrityError as e:
        return render_to_response("error_response.html", {"message": e})

    email = User.objects.get(username=name).email
    output = '''
    <html>
      <head>
        <title>
          Connecting to the model
        </title>
      </head>
      <body>
        <h1>
          Connecting to the model
        </h1>
        The new user's email: %s
      </body>
    </html>''' % (
        email
    )
    return HttpResponse(output)


def add_module(request,name,password,module,activationcode):
    user = User.objects.get(username=name)
    if user.check_password(password):
        if module is not None:
            student = user.student
            if student.modules:
                student.modules = (student.modules + ',' +module)
            else:
                student.modules = module
            student.save()
    output = '''
        <html>
          <head>
            <title>
              Connecting to the model
            </title>
          </head>
          <body>
            <h1>
              Connecting to the model
            </h1>
            The module added was: %s
          </body>
        </html>''' % (
        user.student.modules + activationcode
    )
    return HttpResponse(output)


def login(request, name, password):
    user = User.objects.get(username = name)
    if user.check_password(password):
        output = '''
            <html>
              <head>
                <title>
                  Connecting to the model
                </title>
              </head>
              <body>
                <h1>
                  Password was correct
                </h1>
                The falling user was logged in: %s
                The users modules where: %s
              </body>
            </html>''' % (
            name, user.student.modules)
        return HttpResponse(output)
    else:
        output = '''
            <html>
              <head>
                <title>
                  Connecting to the model
                </title>
              </head>
              <body>
                <h1>
                  Error logging in
                </h1>
                u fucked up or we fucked up, the jist of it is someone fucked up.
              </body>
            </html>'''
        return HttpResponse(output)
