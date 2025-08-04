from django import forms

from . models import Task

class TaskForm(forms.Form):
    task_title = forms.CharField(label='Aufgabentitel', max_length=200)
    task_description = forms.CharField(label='Aufgabenbeschreibung', max_length=2048)

