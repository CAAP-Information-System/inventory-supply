from rest_framework import serializers
from .models import *
class InventorySerializer(serializers.Serializer):
    class Meta:
        model = Inventory
        fields = '__all__'