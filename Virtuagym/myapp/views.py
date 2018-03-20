from django.shortcuts import render
from .models import Exercise
from .models import Plan
from django.contrib.auth.decorators import login_required


    # ...
# Create your views here.
def home(request):
    plans = Plan.objects.all()
    return render(request, 'home.html', {'plans': plans})

def exercise(request,pk):
	exercise=Exercise.objects.get(pk=pk)
	return render(request, 'exercise.html', {'exercise': exercise})

def exercise_all(request):
	exercises=Exercise.objects.all()
	return render(request, 'all_exercise.html', {'exercises': exercises})
