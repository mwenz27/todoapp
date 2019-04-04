from django.shortcuts import render, redirect
from .models import TodoList, TodoItem
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

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
    if request.method != 'POST':
        single_todo_list = TodoList.objects.get(id=title_id)
        items_to_that_list = single_todo_list.todoitem_set.order_by('-date_created')
        context = {'single_todo_list': single_todo_list, 'items_to_that_list': items_to_that_list}
        return render(request, 'page/single_todo_list.html', context)
    else:
        print('########', request.POST)
        # print('##title ID', title_id)
        r = request.POST.getlist("item_id") # use this getlist
        # pull items.ids,  and use python code

        for id_in_record in r:
            # # Selecting the record on that list
            todo = TodoItem.objects.get(pk=id_in_record)
            # # modify that specific record to save it
            todo.done = True
            # # saving that item
            todo.save()


        single_todo_list = TodoList.objects.get(id=title_id)
        items_to_that_list = single_todo_list.todoitem_set.order_by('-date_created')
        context = {'single_todo_list': single_todo_list, 'items_to_that_list': items_to_that_list}
        return render(request, 'page/single_todo_list.html', context)
        # return HttpResponse('hi')

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

