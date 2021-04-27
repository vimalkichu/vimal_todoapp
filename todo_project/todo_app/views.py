from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import Todoforms
from .models import Task
# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home_view.html'
    context_object_name = 'obj1'
class TaskDetailView(DetailView):
    model=Task
    template_name ='detail.html'
    context_object_name = 'i'
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

def home_view(request):
    obj1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        obj=Task(name=name,priority=priority,date=date)
        obj.save()
    return render(request,'home_view.html',{'obj1':obj1})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})
def update(request,id):
    task1=Task.objects.get(id=id)
    form=Todoforms(request.POST or None,instance=task1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task1':task1,'form':form})