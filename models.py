from datetime import date
from django.db import models


class Course(models.Model):
    Course_Name = models.CharField(max_length=20, default='', null=False,blank=False, primary_key=True)
    Duration = models.CharField(max_length=40, default='', null=False, blank=False)
    Image = models.ImageField(default='', upload_to="course_images/", null=False, blank=False)
    Description = models.TextField(max_length=400,  default="", null=False, blank=False)
    Material = models.FileField(default='', upload_to="Course_materials/", null=False,blank=False)
    Price = models.IntegerField(default='')

    def __str__(self):
        return self.Course_Name


class Learner(models.Model):
    Name = models.CharField(max_length=20, default='')
    Gender = models.CharField(max_length=6, default='')
    Email = models.EmailField(max_length=50,default='',primary_key=True)
    DoB = models.DateField(default='')
    Profession = models.CharField(max_length=20, default='')
    Country = models.CharField(max_length=20, default='')
    Number = models.IntegerField(default='')
    Course = models.CharField(max_length=15, default='')
    Language = models.CharField(max_length=16, default='')
    Password = models.CharField(max_length=8, default='')
    Staff = models.CharField(max_length=25, default='')
    joined_on = models.DateField(auto_now_add=True, blank=True)
    Start = models.DateField(default='')
    time = models.CharField(default='', max_length=20)

    def __str__(self):
        return self.Name+", "+self.Staff


class Instructor(models.Model):
    Name = models.CharField(max_length=29, default='')
    Gender = models.CharField(max_length=7, default='')
    Email = models.EmailField(max_length=50, default='', primary_key=True)
    Country = models.CharField(max_length=25, default='')
    Contact = models.CharField(max_length=15, default='')
    Course = models.CharField(max_length=25, default='')
    Qualification = models.CharField(max_length=25, default='')
    Language = models.CharField(max_length=25, default='')
    Profile = models.ImageField(default='', upload_to="Profile/")
    Graduate = models.ImageField(default='', upload_to="Graduation/")
    Experience = models.ImageField(default='', upload_to="Experience/")
    Password = models.CharField(max_length=6, default='')
    Bio = models.TextField(max_length=200, default='')
    Status = models.CharField(max_length=30, default='Pending')

    def __str__(self):
        return self.Name+", "+self.Status


class Staff(models.Model):
    Staff_Name = models.EmailField(max_length=20, default='',primary_key=True)
    Password = models.CharField(max_length=6, default='')

    def __str__(self):
        return self.Staff_Name
