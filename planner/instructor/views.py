from django.shortcuts import render
from django.http import HttpResponse
from .models import instructor

#def instructor (request):
 #return HttpResponse ( 'instructor page')


def instructor_list(request):
    instructor_names = instructor.objects.all()
    context1 = {'instructors': instructor_names}
    return render(request, 'ops.html', context1)


# {% for instructor in instructors %}
 #                                   <option>{{ instructor.instructor_name }}</option>
  #                              {% endfor %}
  #эта вставка работала в ops в упражнениях