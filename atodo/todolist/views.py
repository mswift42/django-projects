from django.shortcuts import render_to_response
from django.http import HttpResponse
from todolist.models import List

def status_report(request):
    todo_listing = []

    for todo_list in List.objects.all():
        todo_dict = {}
        todo_dict['list_object'] = todo_list
        todo_dict['item_count'] = todo_list.item_set.count()
        todo_dict['items_complete'] = todo_list.item_set.filter(completed=True).count()
        todo_dict['percent_complete'] = int(float(todo_dict['items_complete']) / todo_dict['item_count'] * 100)
        todo_listing.append(todo_dict)
    return render_to_response('status_report.html', {'todo_listing': todo_listing})

def status_two(request):
    return HttpResponse("Hallo report")
    
# Create your views here.

def index(request):
    return HttpResponse("Some stuff for later.")
