from django.shortcuts import render,redirect
from .models import ToDo_Model
from django.urls import reverse

def index(request):
    heading = "Django To-Do WebApp"
    if request.method == "POST":
        title = request.POST['title']
        details = request.POST['details']
        date = request.POST['date']

        # print('title is',title,'details is',details,'date is',date);
        if title is None and details is None and date is None:
            print("empty input field")
        else:
            data = ToDo_Model.objects.create(title=title, details=details, Date=date)
            data.save()
            print("data saved successfully")
            return redirect(reverse('get_todo'))
        
    elif request.method == "GET":
        all_data = ToDo_Model.objects.all()
    
    dict = {'heading':heading, 'all_data': all_data}
    return render(request, 'index.html',dict)


def get_todo_lits(request):
    all_data = ToDo_Model.objects.all()
    dict = { 'all_data': all_data}
    return render(request, 'index.html',dict)

def remove_todo_item(request,id):
    data = ToDo_Model.objects.get(id=id)
    data.delete()
    return redirect(reverse('get_todo'))