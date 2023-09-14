from django.db import models

# Create your models here.
class Inventory(models.Model):  
    CATEGORY_CHOICES = [
        ('Motor Vehicles', 'Motor Vehicles'),
        ('Aircraft and Aircrafe Ground Equipment', 'Aircraft and Aircrafe Ground Equipment'),
        ('Other Transportation Equipment', 'Other Transportation Equipment'),
        ('Disaster Response and Rescue Equipment', 'Disaster Response and Rescue Equipment'),
        ('Land', 'Land'),
        ('Other Land Improvements', 'Other Land Improvements'),
        ('Sewer Systems', 'Sewer Systems'),
        ('Power Supply Systems', 'Power Supply Systems'),
        ('Airport Systems', 'Airport Systems'),
        ('Airport Equipment', 'Airport Equipment'),
        ('Buildings', 'Buildings'),
        ('Other Structures', 'Other Structures'),
        ('Office Equipment', 'Office Equipment'),
        ('Furniture & Fixtures', 'Furniture & Fixtures'),
        ('Other Property Plant and Equipment', 'Other Property Plant and Equipment'),
        ('Information and Communication Technical Equipment', 'Information and Communication Technical Equipment'),
        ('Communication Equipment', 'Communication Equipment'),
        ('Medical Equipment', 'Medical Equipment'),
        ('Technical and Scientific Equipment', 'Technical and Scientific Equipment'),
        ('Other Equipment', 'Other Equipment'),
        
    ]
    TYPE_CHOICES = [
        ('Semi-expendable Equipment', 'Semi-expendable Equipment'),
        ('Non-expended Equipment', 'Non-expended Equipment'),
    ]
    inv_type = models.CharField(max_length=100, choices=TYPE_CHOICES, null= True)
    inv_quantity = models.IntegerField(null=True)
    inv_description = models.TextField(max_length=2**31-1, null=True)  
    inv_property = models.CharField(max_length=100, null=True)
    inv_model = models.CharField(max_length=100, null=True)
    inv_serial = models.CharField(max_length=100, null=True)
    inv_acqDate = models.DateField(null=True)   
    inv_acqCost = models.FloatField(null=True)
    inv_accountable = models.IntegerField( null=True) 
    inv_loc = models.CharField(max_length=100, null=True) 
    inv_class = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=  True)


    class Meta:  
        db_table = "inventories"