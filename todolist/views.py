from django.shortcuts import render, redirect
from .models import TodoList, TodoItem
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import pprint

from .forms import TodoItemForm, TodoListForm

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
    if request.method == 'POST':
        # print('########', request.POST)
        # print('##title ID', title_id)
        r = request.POST.getlist("item_id") # use this getlist, this creates a new name
        # pull items.ids,  and use python code

        for id_in_record in r:
            # # Selecting the record on that list
            todo = TodoItem.objects.get(pk=id_in_record)
            # # modify that specific record to save it
            todo.done = True
            # # saving that item
            todo.save()


    # Select one Item
    single_todo_list = TodoList.objects.get(id=title_id)
    ## todoitem_set
    items_to_that_list = single_todo_list.todoitem_set.order_by('-date_created')
    # send data to the html page this is done with a dictionary
    context = {'single_todo_list': single_todo_list, 'items_to_that_list': items_to_that_list}
    return render(request, 'page/single_todo_list.html', context)
    # return HttpResponse('hi')


def new_topic(request):
    '''Add a new topic'''
    print(request.POST)
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TodoListForm()
    else:
        # POST data submitted; process data.
        form = TodoListForm(data=request.POST)
        # print('####-----#####', form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todolist:todo'))

    context = {'form': form}
    return render(request, 'page/new_topic.html', context)


def new_entry(request, title_id):
    '''entry for a list'''
    print('GET RESPONSE###########', request.GET)

    todolist = TodoList.objects.get(id=title_id)

    if request.method != 'POST':
        # No data submitted; create a blank form
        form = TodoItemForm()
    else:
        # Post data submitted; processed data
        form = TodoItemForm(data=request.POST)
        # print('####-----#####', form)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.todolist = todolist
            new_entry.save()
            return HttpResponseRedirect(reverse('todolist:new_entry', args=[title_id]))
            # return HttpResponse('hi 1 post response')

    context = {'todolist': todolist, 'form': form}
    print('#########', todolist)
    # pprint(context)
    return render(request, 'page/new_entry.html', context)
    # return HttpResponse('hi 2 get response')

def edit_entry(request, entry_id):
    '''edit existing entry'''
    entry = TodoItem.objects.get(id=entry_id)
    topic = entry.names

    if request.method != 'POST':
        # Initial request
        form = TodoItemForm(instance=entry)
    else:
        form = TodoItemForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todolist:todo', args=[title.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request,  'page/new_entry.html', context)




# submit a form to update the items in the todolist

## when a post request is comming select the record to the database

# then return the thing

# def new_topic(request):
#     """Add a new topic."""
#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = TopicForm()
#     else:
#         # POST data submitted; process data.
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('learning_logs:topics'))
#     context = {'form': form}
#     return render(request, 'learning_logs/new_topic.html', context)
#

# @require_POST


# def complete_one_item_todo(request, item_id):
#     # If the method is GET leave the item as it is
#     if request.method != 'POST':
#         return redirect('page/single_todo_list.html')
#     else:

