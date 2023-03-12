from django.shortcuts import render
from django.http import HttpResponse
from .models import instructors
# Create your views here.
def instructors (request):
    return HttpResponse ( 'instructors page')