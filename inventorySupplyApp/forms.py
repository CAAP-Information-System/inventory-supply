from django import forms  
from .models import *  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewInventoryForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        model = Inventory
        fields = '__all__'