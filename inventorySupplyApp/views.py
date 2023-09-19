# views.py
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect,
                              HttpResponse,
                              redirect)
from .models import *
from .forms import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework import generics
from .serializers import InventorySerializer
from django.db.models import Q
from django.template import loader



class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

# Create your views here.
# def home(request):

#     obj = get_object_or_404(Inventory, id = id)
 
 
#     if request.method =="POST":
#         obj.delete()
#         return HttpResponseRedirect("/")
 
#     inventory = Inventory.objects.all()  
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         inventory = Inventory.objects.filter(
#             Q(inv_type__icontains=searched) |
#             Q(inv_model__icontains=searched) |
#             Q(inv_serial__icontains=searched) |
#             Q(inv_loc__icontains=searched)
            
#         )
#         filtered_letter = Inventory.objects.filter(inv_loc__istartswith=searched).order_by('inv_loc')
#         return render(request, 'components/home.html',{'inventory': inventory, 'searched':searched, 'filtered_letter':filtered_letter})
#     else:
#         return render(request, 'components/home.html',{'inventory': inventory,})
    
def SearchProject(request):
    value = request.POST['search']
    inventory = Inventory.objects.filter(Q(inv_quantity__icontains=value) | Q(inv_class__icontains=value)).order_by('inv_type')
    return render(request, 'components/home.html',{'inventory': inventory,})
    
    
def home_sort_by_type(request):
    inventory = Inventory.objects.order_by('inv_type').values()
    return render(request, 'components/home.html', {'inventory': inventory})


def home(request, sort_order='asc'):

    if sort_order == 'asc':
        inventory = Inventory.objects.order_by('inv_description')
        inventory = Inventory.objects.order_by('inv_loc')
        toggle_sort_order = 'desc'
    else:
        inventory = Inventory.objects.order_by('inv_description')
        inventory = Inventory.objects.order_by('-inv_loc')
        toggle_sort_order = 'asc'

    context = {
        'inventory': inventory,
        'toggle_sort_order': toggle_sort_order,
    }

    return render(request, 'components/home.html', context)

def add_inventory(request):
    context = {}
    form = NewInventoryForm(request.POST or None)
    context['form']= form
    if form.is_valid():
        form.save()
        messages.success(request, 'New inventory Added.') 
        return HttpResponseRedirect("/")
    # if request.GET:
    #     temp = request.GET['inv_acqDate']   
    #     print(type(temp))
    return render(request, "crud/add.html", context)

def view_inventory(request,id):
    context ={}
 
    # add the dictionary during initialization
    context["view"] = Inventory.objects.get(id = id)
         
    return render(request, "crud/view.html", context)

def edit_inventory(request,id):
    context = {}
    inventory = Inventory.objects.get(id=id)  
    form = NewInventoryForm(request.POST, instance = inventory)  
    if form.is_valid():  
        form.save()  
        return redirect("/")
        
    return render(request, 'crud/edit.html', {'inventory': inventory})  

def update_inventory(request, id):
    context ={}
    obj = get_object_or_404(Inventory, id = id)
    form = NewInventoryForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")

    context["update"] = form
 
    return render(request, "crud/update.html", context)

def delete_inventory(request, id):
    context = {}
    obj = get_object_or_404(Inventory, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "crud/home.html", context)