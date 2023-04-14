from django import forms
from instructor.models import instructor
from student.models import student


class InstrForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import instructor
        self.fields['list'] = forms.ModelChoiceField(queryset=student.objects.all(), label='Студент', widget=forms.Select(attrs={
        'class': 'form-select',
        'placeholder': 'Введите группу студента'}))

    class Meta:
        model = instructor
        fields = '__all__'
