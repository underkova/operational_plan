from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import student
from django.shortcuts import render
from .models import briefing
from .models import exercise
from django.contrib.auth.decorators import login_required

__all__ = (
    'ops', 'test',
)

@login_required
def ops(request):
    student_names = student.objects.all().order_by('name')
    brif = briefing.objects.all()
    ex = exercise.objects.all()
    context = {'students': student_names, 'briefings': brif, 'exercises': ex,}
    return render(request, 'students.html', context)

def test(request, pk=None):
    
    brif = briefing.objects.all()
    context1 = {'briefing': brif}
    return render(request, 'main_tpl.html', context1)
