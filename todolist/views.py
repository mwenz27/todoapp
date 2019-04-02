from django.shortcuts import render
from .models import TodoList, TodoItem
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.


def home(request):
    item = TodoList.objects.all()
    return render(request, 'page/home.html', {'item': item})


def todo(request):
    complete_list = TodoList.objects.all()
    context = {'complete_list': complete_list}
    return render(request, 'page/todo.html', context)




## show single list with all the entries


def single_todo_list(request, title_id):
    print(request.POST)
    single_todo_list = TodoList.objects.get(id=title_id)
    items_to_that_list = single_todo_list.todoitem_set.order_by('-date_created')
    context = {'single_todo_list': single_todo_list, 'items_to_that_list': items_to_that_list}
    return render(request, 'page/single_todo_list.html', context)


# submit a form to update the items in the todolist




