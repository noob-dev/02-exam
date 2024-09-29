from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['name', 'email', 'question']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control',
            }),
            'question': forms.Textarea(attrs={
                'placeholder': 'Enter your question',
                'class': 'form-control',
            }),
        }