from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import students
from .models import students
from django.shortcuts import render

def student_list(request):
    student_names = students.objects.all().order_by('name')
    context = {'student_names': student_names}
    return render(request, 'planner.html', context)

def index (request):
    return HttpResponse('main page') #будет просто текст

def about (request):
    return HttpResponse('description page') #тоже текст
# Create your views here.
