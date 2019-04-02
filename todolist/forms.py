from django import forms

from .models import TodoItem, TodoList

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
