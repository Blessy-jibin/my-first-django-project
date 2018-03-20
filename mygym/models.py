from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Day(models.Model):
    day_number = models.CharField(max_length=100,unique=True)
    exercise = models.ManyToManyField(Exercise,null=True)

    def __str__(self):
        return self.day_number

class Plan(models.Model):
    title = models.CharField(max_length=100)
    
    day = models.ManyToManyField(Day)

    def __str__(self):
        return self.title


class UserData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    plan = models.ManyToManyField(Plan)

    def __str__(self):
        return self.user.username


