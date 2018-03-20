from django.contrib import admin

from .models import (Plan, Day, Exercise,UserData)

admin.site.register(Plan)
admin.site.register(Day)
admin.site.register(Exercise)
admin.site.register(UserData)

