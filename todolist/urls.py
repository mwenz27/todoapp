from django.urls import path
from todolist import views

app_name = 'todolist'

urlpatterns = [
    # home page
    path('', views.todo, name='home'),

    path('todo/', views.todo, name='todo'),
    # detail page for a single topic
    path('todo/<int:title_id>', views.single_todo_list, name='single_todo_list'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:title_id>', views.new_entry, name='new_entry'),
    path('edit_entry/<int:title_id>', views.edit_entry, name='edit_entry'),

]