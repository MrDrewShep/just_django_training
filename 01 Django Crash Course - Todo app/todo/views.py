from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.
# See below alternate ways of providing an HttpResponse
# def todo_list(request):
#     return HttpResponse("Howdy")

# References the `templates` folder in the project directory
# def todo_list(request):
#     return render(request, "todo_list.html")

# References the `templates` folder in this app directory
# def todo_list(request):
#     return render(request, "todo/todo_list.html")

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        "todo_list": todos
    }
    return render(request, "todo/todo_list.html", context)

def todo_detail(request, id):
    todo = Todo.objects.get(id=id)
    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)

def todo_create(request):
    # This line enables us to use the same endpoint whether the 
    # request is GET (I want to fill out a blank form) or 
    # POST (I just hit `submit` on my form)
    form = TodoForm(request.POST or None)
    if form.is_valid():
        """
        # OPTION 1: The long way to save a new todo
        # `form.cleaned_data()` method
        print(form.cleaned_data)
        name = form.cleaned_data['name']
        due_date = form.cleaned_data['due_date']
        # create a todo object
        new_todo = Todo.objects.create(name=name, due_date=due_date)
        """
        # OPTION 2: The shortcut, because we used a ModelForm object
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "todo/todo_create.html", context)