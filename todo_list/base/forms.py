from django import forms
from .models import Task
class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at','importance', 'category', 'subjects', 'objects_of_plening']
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'},),
        }
class RegisterForm(forms.Form):
    username = forms.CharField(label='Ім\'я користувача')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    email = forms.EmailField(label='Email',widget=forms.EmailInput())

class LoginForm(forms.Form):
    username = username = forms.CharField(label='Ім\'я користувача')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

