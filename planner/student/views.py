from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import student
from django.shortcuts import render
from .models import briefing
from .models import exercise
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import StudForm

__all__ = (
    'ops', 'list', 'StudDetailView', 'StudCreateView', 'StudUpdateView', 'StudDeleteView'
)


@login_required
def ops(request):
    student_names = student.objects.all().order_by('name')
    brif = briefing.objects.all()
    ex = exercise.objects.all()
    context = {'students': student_names, 'briefings': brif, 'exercises': ex, }
    return render(request, 'student/students.html', context)


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
