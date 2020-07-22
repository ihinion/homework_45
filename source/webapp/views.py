from django.shortcuts import render
from webapp.models import Task
from django.shortcuts import redirect
from webapp.models import STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.all()
    options = STATUS_CHOICES
    context = {'tasks': tasks, 'options': options}
    return render(request, 'index.html', context)


def task_create_view(request):
    options = STATUS_CHOICES
    if request.method == 'GET':
        context = {
            'options': options
        }
        return render(request, 'add.html', context)
    elif request.method == 'POST':
        description = request.POST.get('description')
        status = request.POST.get('status')
        finish_date = request.POST.get('finish_date')
        if finish_date:
            Task.objects.create(description=description, status=status, finish_date=finish_date)
        else:
            Task.objects.create(description=description, status=status)
        return redirect(index_view)