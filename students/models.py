from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone = models.CharField(max_length=15, blank=False, unique=True)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    


    