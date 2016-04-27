from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Lecture, Notes
from django.http import FileResponse

# Create your views here.


def create(request,module,lname,password):
    user = User.objects.get(username=lname)
    if Lecture.objects.filter(module_code = module).exists():
        output = '''
            <html>
              <head>
                <title>
                  This Module Exists Yo!
                </title>
              </head>
              <body>
                <h1>
                  YOU TRYING TO FUCK WITH ME BOOOOOOI
                </h1>
                %s get out of here
              </body>
            </html>''' % (
            lname
        )
        return HttpResponse(output)
    else:
        if user:
            if user.check_password(password):
                lecture = Lecture.objects.create(module_code=module, lecturer_name=lname)
                lecture.save()
                output = '''
                    <html>
                      <head>
                        <title>
                          YOU FUCKING DID IT!
                        </title>
                      </head>
                      <body>
                        <h1>
                          YOU FUCKING DID IT!
                        </h1>
                        YOU DID IT SENIOR POPPY or : %s
                      </body>
                    </html>''' % (
                    lname
                )
                return HttpResponse(output)


def add_notes(request,module,lname,password,notesname):
    lecture = Lecture.objects.get(module_code = module)
    user = User.objects.get(username=lname)
    if lecture:
        if user.check_password(password):
            notes = Notes.objects.create(lecture_name=lecture, notes_name=notesname, notes=request.FILES['notes'])
            notes.save()
            output = '''
                <html>
                  <head>
                    <title>
                      YOU FUCKING DID IT!
                    </title>
                  </head>
                  <body>
                    <h1>
                      YOU FUCKING DID IT!
                    </h1>
                    YOU DID IT SENIOR POPPY or : %s %s
                  </body>
                </html>''' % (
                notes.notes_name, notes.notes.path
            )
            return HttpResponse(output)

def get_notes(request,module):
    lecture = Lecture.objects.get(module_code=module)
    note = Notes.objects.get(lecture_name=lecture)
    if note:
        response = FileResponse(open(note.notes.path, 'rb'))
        return response
