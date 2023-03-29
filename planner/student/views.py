from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import student
from .models import student
from django.shortcuts import render
from .models import exercise
from django.contrib.auth.decorators import login_required

@login_required
def student_list(request):
    student_names = student.objects.all().order_by('name')
    context = {'students': student_names}
    return render(request, 'ops_stud.html', context)

def index (request):
    return HttpResponse ('main page')

def about (request):
    return HttpResponse('description page')

def exercise_list(request):
    exercises = exercise.objects.all().order_by('exercise_code')
    context2 = {'exercises': exercises}
    return render(request, 'ops.html', context2)
