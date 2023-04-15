from django import forms
from instructor.models import instructor
from student.models import student


class StudForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=student.objects.all(), label='Студент', required=False,
                                         widget=forms.SelectMultiple(attrs={
                                        'class': 'form-control js-multiple',}))
    class Meta:
        model = instructor
        fields = 'students',

class InstrForm(forms.ModelForm):
    instructors = forms.ModelChoiceField(queryset=student.objects.all(), label='Студент', widget=forms.Select(attrs={
    'class': 'form-select',
    'placeholder': 'Введите группу студента'}))
    class Meta:
        model = instructor
        fields = 'instructors',