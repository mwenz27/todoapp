from django import forms

from .models import TodoItem, TodoList


## LIST

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'completed']
        labels = {'title': 'Please enter a new Topic',
                  'completed': 'Default is set to zero'}


# ENTRY TO THE LIST


class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['name', 'description', 'due_date']
        labels = {'name': 'Please enter a new item of this',
                  'description': 'Small blurb about this the item',
                  'due_date': 'Enter a due date Y-M-D'}



