from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import student, briefing, exercise, Plan
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import StudForm, PlanForm
from django.shortcuts import redirect
from django.db.models import Sum
from django.db import models
import datetime
from django.contrib import messages
from datetime import date
from django.utils.translation import activate

__all__ = (
    'ops', 'list', 'StudDetailView', 'StudCreateView', 'StudUpdateView', 'StudDeleteView', 'plan', 'delete_all_plans'
)


@login_required
def ops(request):
    student_names = student.objects.all().order_by('name')
    brif = briefing.objects.all()
    ex = exercise.objects.all()
    context = {'students': student_names, 'briefings': brif, 'exercises': ex, }
    return render(request, 'student/students.html', context)

def plan(request):
    activate('ru')  # Активируем русскую локализацию
    current_date = date.today()
    exercises = exercise.objects.all()
    students = student.objects.all()
    plans = Plan.objects.all()
    total_time = Plan.objects.aggregate(total_time=Sum('time'))
    total_approaches = Plan.objects.aggregate(total_approaches=Sum('approaches'))
    total_landings = Plan.objects.aggregate(total_landings=Sum('landings'))
    total_info_per_student = Plan.objects.values('student').annotate(
        total_time=Sum('time'),
        approaches=Sum('approaches'),
        landings=Sum('landings')
    )
    for info in total_info_per_student:
        if info['total_time'] > datetime.timedelta(hours=4):
            message = f"Внимание! Общее время для студента {info['student']} превышает предельное значение"
            messages.error(request, message)
        elif info['total_time'] > datetime.timedelta(hours=3):
            message = f"Внимание! Общее время для студента {info['student']} превышает 3 часа"
            messages.warning(request, message)

    if total_time['total_time'] is not None and total_time['total_time'] > datetime.timedelta(hours=6):
        message = 'Внимание: Общее время превышает 6 часов!'
        messages.error(request, message)
    else:
        message = None

    if request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            student_input = form.cleaned_data['student']
            exercise_input = form.cleaned_data['exercise']
            exercise_obj = exercise.objects.get(pk=exercise_input.id)
            total_time = exercise_obj.total_time
            approaches = exercise_obj.approaches
            landings = exercise_obj.landings

            time_input = form.cleaned_data.get('time')
            if time_input:
                total_time = time_input

            approaches_input = form.cleaned_data.get('approaches')
            if approaches_input:
                approaches = approaches_input

            landings_input = form.cleaned_data.get('landings')
            if landings_input:
                landings = landings_input
            planDB = Plan(student=student_input, time=total_time, exercise=exercise_input, approaches=approaches, landings=landings)
            planDB.save()
    else:
        form = PlanForm()
    return render(request, 'student/students.html', {'exercises': exercises,
                                                     'plans': plans,
                                                     'students': students,
                                                     'form': form,
                                                     'total_time': total_time,
                                                     'total_approaches': total_approaches,
                                                     'total_landings': total_landings,
                                                     'student_info': total_info_per_student,
                                                     'current_date': current_date,})

def list(request, pk=None):
    if request.method == 'POST':
        form = StudForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = StudForm()
    stud = student.objects.all()
    lst = Paginator(stud, 8)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'student/list.html', context)


class StudDetailView(DetailView):
    queryset = student.objects.all()
    template_name = 'student/detail.html'


class StudCreateView(SuccessMessageMixin, CreateView):
    model = student
    form_class = StudForm
    template_name = 'student/create.html'
    success_url = reverse_lazy('student:list')
    success_message = "Студент успешно создан"




class StudUpdateView(SuccessMessageMixin, UpdateView):
    model = student
    form_class = StudForm
    template_name = 'student/update.html'
    success_url = reverse_lazy('student:list')
    success_message = "Студент успешно отредактирован"


class StudDeleteView(SuccessMessageMixin, DeleteView):
    model = student
    template_name = 'student/delete.html'
    success_url = reverse_lazy('student:list')
    success_message = "Студент успешно удален"

def delete_all_plans(request):
    if request.method == 'POST':
        Plan.objects.all().delete()
        return redirect('student:plan')
    else:
        return redirect('student:plan')


