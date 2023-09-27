# views.py
from .forms import *
from django.contrib import messages
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
from collections import Counter



class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


def SearchProject(request):
    value = request.POST['search']
    inventory = Inventory.objects.filter(
        Q(inv_type__icontains=value) |
        Q(inv_quantity__icontains=value) | 
        Q(inv_description__icontains=value) |
        Q(inv_model__icontains=value) |
        Q(inv_serial__icontains=value) |
        Q(inv_acqCost__icontains=value) |
        Q(inv_acqDate__icontains=value) |
        Q(inv_loc__icontains=value) |
        Q(inv_class__icontains=value) 

        
        ).order_by('inv_type')
    return render(request, 'components/home.html',{'inventory': inventory,})
    

def home(request, sort_order='asc'):
    motorv = Inventory.objects.filter(inv_class='Motor Vehicles').count()
    aage = Inventory.objects.filter(inv_class='Aircraft and Aircrafe Ground Equipment').count()
    ote = Inventory.objects.filter(inv_class='Other Transportation Equipment').count()
    drre = Inventory.objects.filter(inv_class='Disaster Response and Rescue Equipment').count()
    land = Inventory.objects.filter(inv_class='Land').count()
    oli = Inventory.objects.filter(inv_class='Other Land Improvements').count()
    ss = Inventory.objects.filter(inv_class='Sewer Systems').count()
    pps = Inventory.objects.filter(inv_class='Power Supply Systems').count()
    aps = Inventory.objects.filter(inv_class='Airport Systems').count()
    aep = Inventory.objects.filter(inv_class='Airport Equipment').count()
    bld = Inventory.objects.filter(inv_class='Buildings').count()
    oths = Inventory.objects.filter(inv_class='Other Structures').count()
    offeq = Inventory.objects.filter(inv_class='Office Equipment').count()
    ff = Inventory.objects.filter(inv_class='Furniture & Fixtures').count()
    oppe = Inventory.objects.filter(inv_class='Other Property Plant and Equipment').count()
    ict = Inventory.objects.filter(inv_class='Information and Communication Technical Equipment').count()
    comm = Inventory.objects.filter(inv_class='Communication Equipment').count()
    med = Inventory.objects.filter(inv_class='Medical Equipment').count()
    techsci = Inventory.objects.filter(inv_class='Technical and Scientific Equipment ').count()
    other = Inventory.objects.filter(inv_class='Other Equipment').count()
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
        'motorv' : motorv,
        'aage': aage,
        'drre': drre,
        'land': land,
        'ote':ote,
        'oli': oli,
        'ss': ss,
        'pps': pps,
        'aps':aps,
        'aep': aep,
        'bld': bld,
        'oths': oths,
        'offeq': offeq,
        'ff': ff,
        'oppe': oppe,
        'ict': ict,
        'comm': comm,
        'med': med,
        'techsci': techsci,
        'other': other
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
    return render(request, "crud/add.html", context)

def view_inventory(request,id):
    context ={}
    inventories = Inventory.objects.all()
    view = Inventory.objects.get(id = id)
    for inv in inventories:
        inv.totalValue = inv.inv_acqCost * inv.inv_quantity
         
    return render(request, "crud/view.html", {'view': view, 'inventories': inventories},)

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


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Inventory, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "crud/view.html", context)

def delete_inventory(request, id):
    context = {}
    obj = get_object_or_404(Inventory, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "crud/home.html", context)

def error_404(request):
    return render(request, "error_template/404.html")