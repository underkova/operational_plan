from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


__all__ = (
    'index',
)
@login_required
def index(request):
    return render(request, 'main.html')

