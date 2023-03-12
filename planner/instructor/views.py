from django.shortcuts import render
from django.http import HttpResponse
from .models import instructor
# Create your views here.
def instructor (request):
    return HttpResponse ( 'instructor page')