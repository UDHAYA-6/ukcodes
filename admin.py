from .models import Course, Learner, Instructor, Staff
from django.contrib import admin
from django.contrib.admin import register

admin.site.register(Learner)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Staff)
