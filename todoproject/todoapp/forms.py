from .models import *
from django import forms

class TodoForm(forms.ModelForm):

    class Meta:
        model=Task
        fields=['task', 'priority', 'date']