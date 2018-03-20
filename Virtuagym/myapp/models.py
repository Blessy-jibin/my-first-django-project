from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Exercise(models.Model)

    exercise_name=models.CharField(max_length=30)
    def __str__(self):
        return self.exercise_name


class Day(models.Model):
    day_number = models.CharField(unique=True,max_length=30)
    exercise=models.ForeignKey(Exercise, related_name='dayex',on_delete=models.CASCADE)
    
    return self.Day_name


class Plan(models.Model):
    name = models.CharField(max_length=15, unique=True)
    day = models.ForeignKey(Day, related_name='planday',on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name


