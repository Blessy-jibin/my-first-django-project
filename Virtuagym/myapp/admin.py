from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Exercise
from .models import Day
from .models import Plan


admin.site.register(Exercise)
admin.site.register(Plan)

admin.site.register(Day)