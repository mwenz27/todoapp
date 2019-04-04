from django.urls import path
from todolist import views

app_name = 'todolist'

urlpatterns = [
    # home page
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    # detail page for a single topic
    path('todo/<int:title_id>', views.single_todo_list, name='single_todo_list'),

]