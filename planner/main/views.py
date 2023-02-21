from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse ('main page')

def about (request):
    return HttpResponse('description page')

def students (request):
    return HttpResponse('planner.html') # здесь вернет шаблон

#def instructors (request):
 #   return HttpResponse('instructors page') # при переходе по ссылке instructors выдаст этот текст
# Create your views here.
