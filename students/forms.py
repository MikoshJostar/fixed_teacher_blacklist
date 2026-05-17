from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_class', 'reason', 'debt', 'bad_grade']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ім'я учня"}),
            'student_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Клас або курс'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Причина додавання'}),
        }
