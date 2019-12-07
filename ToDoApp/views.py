from django.shortcuts import render
from django.utils import timezone
from ToDoApp.models import Todo
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request,'ToDoApp/index.html', {
        "todo_items": todo_items
    })

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")

