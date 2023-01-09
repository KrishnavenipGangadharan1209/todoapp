from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import Task
from django.views.generic import *

class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task1'

class UpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task2'
    fields=('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:cbvhome')

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


# Create your views here.
def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        tname = request.POST.get('name', '')
        prior = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(task=tname, priority=prior, date=date)
        task.save()
    return render(request, 'index.html', {'task1': task1})


def delete_task(request, taskid):
    task=Task.objects.get(id= taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request,id):
    task= Task.objects.get(id=id)
    form1=TodoForm(request.POST or None, instance=task)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form1':form1,'tsak':task})