from django.shortcuts import render
from webapp.models import Task
from django.shortcuts import redirect
from webapp.models import STATUS_CHOICES


def index_view(request):
    tasks = Task.objects.all()
    options = []
    for i in STATUS_CHOICES:
        option = {i[0]: i[1]}
        options.append(option)
    context = {'tasks': tasks, 'options': options}
    return render(request, 'index.html', context)
