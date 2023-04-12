from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .models import Task


class TaskList(ListView):
    """
    Returns a list of tasks from the specified model.
    There are attributes that can be customized like context_object_name(the name of the list returned)
    """
    model = Task
    context_object_name = "tasks"


class TaskDetail(DetailView):
    """Returns a task of a specified id"""
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasks')
