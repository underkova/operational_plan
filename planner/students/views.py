from django.shortcuts import render
from django.shortcuts import HttpResponse

def students (request):
    return render (request, 'planner.html') #откроется файл разметки страницы мурата

def index (request):
    return HttpResponse ('main page') #будет просто текст

def about (request):
    return HttpResponse('description page') #тоже текст
# Create your views here.
