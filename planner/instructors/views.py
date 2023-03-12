from django.shortcuts import render
from django.http import HttpResponse
from .models import instructors
# Create your views here.
def instructors_page ():
    return HttpResponse('instructors page')