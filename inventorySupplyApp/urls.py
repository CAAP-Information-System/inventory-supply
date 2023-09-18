from django.urls import path,re_path    
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add_inventory, name='add'),
    path('edit/<int:id>', views.edit_inventory),  
    path('view/<int:id>', views.view_inventory),  
    path('update/<int:id>/', views.update_inventory, name='update'),  
    path('<int:id>/delete', views.delete_inventory, name='delete_inventory'),  
    path('inventory/', views.InventoryList.as_view()),
    path('', views.home_sort_by_type, name='home_sort_by_type'),
    path('<str:sort_order>/', views.home, name='home'),
    path('<str:sort_order>/add', views.add_inventory),


]