from django.shortcuts import render, redirect
from posts.models import Post
from .models import devtools
from .forms import devtoolsForm
# Create your views here.
def list(req):
    tools = devtools.objects.all()
    ctx = {'tools':tools}
    return render(req, 'tools/list.html', ctx)

def create(req):
    if req.method == 'GET':
        form = devtoolsForm()
        ctx = {'form' : form}
        return render(req, 'tools/create.html', ctx)
    form = devtoolsForm(req.POST)
    if form.is_valid():
        form.save()
    return redirect('tools:list')

def delete(req, pk):
    devtools.objects.get(id=pk).delete()
    return redirect('tools:list')

def update(req,pk):
    tool = devtools.objects.get(id=pk)
    if req.method == 'GET':
        form = devtoolsForm(instance=tool)
        ctx = {'form' : form, 'pk':pk}
        return render(req, 'tools/update.html', ctx)
    
    form = devtoolsForm(req.POST, instance=tool)
    if form.is_valid():
        form.save()
        return redirect('tools:list')
    ctx = {'form': form, 'pk': pk}
    return render(req, 'tools/update.html', ctx)

def detail(req, pk):
    tool = devtools.objects.get(id=pk)
    ctx = {'tool': tool}
    return render(req, 'tools/detail.html', ctx)
