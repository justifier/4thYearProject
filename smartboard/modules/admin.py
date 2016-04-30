from django.contrib import admin
from .models import Lecture, Notes, Module, Video, Attachment

# Register your models here.
admin.site.register(Module)
admin.site.register(Lecture)
admin.site.register(Notes)
admin.site.register(Video)
admin.site.register(Attachment)
