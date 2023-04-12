from django import forms
from student.models import student


class StudForm(forms.ModelForm):
    name = forms.CharField(label='ФИО', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ФИО студента'}))
    group = forms.CharField(label='Группа', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите группу студента'}))
    class Meta:
        model = student
        fields = ('name', 'group',)
