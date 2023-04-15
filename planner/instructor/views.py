from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import instructor
from django.shortcuts import render
from student.models import briefing, exercise
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from instructor.forms import InstrForm, StudForm
from django.contrib import messages

__all__ = ('instructor_list', 'list', 'InstrUpdateView',  'InstrDetailView', 'InstrAddStud', 'InstrDeleteView', 'instructor_assign'
)


@login_required
def list(request, pk=None):
    Instr = instructor.objects.all()
    lst = Paginator(Instr, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj,}
    return render(request, 'instructor/list.html', context)

class InstrDetailView(DetailView):
    queryset = instructor.objects.all()
    template_name = 'instructor/detail.html'

class InstrAddStud(SuccessMessageMixin, CreateView):
    model = instructor
    form_class = InstrForm
    template_name = 'instructor/create.html'
    success_url = reverse_lazy('instructor:list')
    success_message = "Студент успешно создан"

class InstrUpdateView(SuccessMessageMixin, UpdateView):
    model = instructor
    form_class = StudForm
    template_name = 'instructor/update.html'
    success_url = reverse_lazy('instructor:instructor_list')
    success_message = "Студенты добавлены"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instr_name'] = self.object.instructor_name
        return context
class InstrDeleteView(SuccessMessageMixin, DeleteView):
    model = instructor
    template_name = 'instructor/delete.html'
    success_url = reverse_lazy('instructor:list')
    success_message = "Студент успешно удален"

def instructor_list(request):
    # if request.method == 'POST':
    #     instrform = InstrForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #         form.save()
    # studform = StudForm()
    # instrform = InstrForm()
    Instr = instructor.objects.all()
    lst = Paginator(Instr, 8)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'instructor/home.html', context)

def instructor_assign(request):
    if request.method == "POST":
        form = StudForm(request.POST)
        a = 1
        return render(request, 'instructor/home.html', {'form': form})
    else:
        form = StudForm()
        messages.error(request, "Нет данных")
        return render(request, 'instructor/home.html', {'form': form})

