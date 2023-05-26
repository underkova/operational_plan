from django import forms
from student.models import student, exercise


class StudForm(forms.ModelForm):
    name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ФИО студента'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import group
        self.fields['group'] = forms.ModelChoiceField(queryset=group.objects.all(), label='Группа', widget=forms.Select(attrs={
        'class': 'form-select',
        'placeholder': 'Введите группу студента'}))


    class Meta:
        model = student
        fields = ('name', 'group',)

class PlanForm(forms.Form):
    student = forms.ModelChoiceField(queryset=student.objects.all(), label='Студент', widget=forms.Select(attrs={
        'class': 'form-select'}))
    exercise = forms.ModelChoiceField(queryset=exercise.objects.all(), label='Группа', widget=forms.Select(attrs={
        'class': 'form-select'}))
    approaches = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))
    landings = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        }))