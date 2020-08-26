from django.conf import settings
from django.db import models
from django.db.models import CharField
from django.utils import timezone
from django.contrib.auth.models import User
import ast, datetime

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.name

class Reference(models.Model):
    name = models.TextField()
    who = models.TextField()
    email = models.CharField(max_length=100)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.name

class TechSkill(models.Model):
    skill = models.TextField()

    def __str__(self):
        return self.skill

class PersonalInterests(models.Model):
    interest = models.TextField()

    def __str__(self):
        return self.interest

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publised_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Education(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()#default=DateField.auto_now)
    course = models.TextField()
    school = models.TextField()

    def __str__(self):
        return self.course

class WorkExperience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.TextField()
    where = models.TextField()

    def __str__(self):
        return self.role

class Person(models.Model):
    me = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    address = models.TextField()

    def add_to_others(self, value):
        self.personal_others.append(value)
        self.save()

    def __str__(self):
        return self.me.username

class Others(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name