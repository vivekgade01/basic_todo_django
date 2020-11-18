from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.utils import timezone
from . import urls
# Create your views here.


@csrf_exempt
def home(request):
    task_list = Todo.objects.all().order_by('-created')
    context = {
        'task_list' : task_list,
    }

    return render(request,'my_app/index.html', context)


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST.get('content')
    created_obj = Todo.objects.create(task=content, created=current_date)
    return HttpResponseRedirect(reverse('my_app:home'))

@csrf_exempt
def delete_todo(request,task_id):
    Todo.objects.get(id = task_id).delete()
    return HttpResponseRedirect(reverse('my_app:home'))
