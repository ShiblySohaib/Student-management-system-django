from django.contrib import admin
from students.models import Student, Course

admin.site.register([Student,Course])