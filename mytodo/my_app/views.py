from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
# Create your views here.


@csrf_exempt
def home(request):
    task_list = Todo.objects.all().order_by('-created')
    context = {
        'task_list' : task_list,
    }

    return render(request,'base.html', context)

@csrf_exempt
def add_todo(request):
    task_text = request.POST.get('task_text')
    current_date = timezone.now()
    task = Todo.objects.create(task = task_text,created=current_date)
    task.save()
    return HttpResponseRedirect("/")