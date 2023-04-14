from django.shortcuts import render
from django.shortcuts import HttpResponse
from instructor.models import instructor
from django.shortcuts import render
from student.models import briefing, exercise
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from instructor.forms import InstrForm

__all__ = ('instructor_list', 'list',
           # 'ops', 'InstrDetailView', 'InstrCreateView', 'InstrUpdateView', 'InstrDeleteView'
)


@login_required
# def ops(request):
#     instructor_names = instructor.objects.all().order_by('name')
#     brif = briefing.objects.all()
#     ex = exercise.objects.all()
#     context = {'instructors': instructor_names, 'briefings': brif, 'exercises': ex, }
#     return render(request, 'instructor/instructors.html', context)


def list(request, pk=None):
    Instr = instructor.objects.all()
    lst = Paginator(Instr, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'instructor/list.html', context)

#
# class InstrDetailView(DetailView):
#     queryset = instructor.objects.all()
#     template_name = 'instructor/detail.html'
#
#
# class InstrCreateView(SuccessMessageMixin, CreateView):
#     model = instructor
#     form_class = InstrForm
#     template_name = 'instructor/create.html'
#     success_url = reverse_lazy('instructor:list')
#     success_message = "Студент успешно создан"
#
#
#
#
# class InstrUpdateView(SuccessMessageMixin, UpdateView):
#     model = instructor
#     form_class = InstrForm
#     template_name = 'instructor/update.html'
#     success_url = reverse_lazy('instructor:list')
#     success_message = "Студент успешно отредактирован"
#
#
# class InstrDeleteView(SuccessMessageMixin, DeleteView):
#     model = instructor
#     template_name = 'instructor/delete.html'
#     success_url = reverse_lazy('instructor:list')
#     success_message = "Студент успешно удален"

def instructor_list(request):
    if request.method == 'POST':
        form = InstrForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = InstrForm()
    Instr = instructor.objects.all()
    lst = Paginator(Instr, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj, 'form': form}
    return render(request, 'instructor/home.html', context)

