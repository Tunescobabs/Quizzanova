
from django import forms
from .models import CustomUser, Question,Answer

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['firstname', 'lastname', 'email']

class AnswerForm(forms.Form):
    class Meta:
        model = Question
        fields =['__all__']
    