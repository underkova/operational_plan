from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index (request):
    return HttpResponse ('main page')

def about (request):
    return HttpResponse('description page')

def students (request):
    return HttpResponse('ops.html') # здесь вернет шаблон

#def instructor (request):
 #   return HttpResponse('instructor page') # при переходе по ссылке instructor выдаст этот текст
# Create your views here.
