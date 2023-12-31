from django.urls import path,re_path    
from . import views

urlpatterns = [
    path('searchbar', views.SearchProject, name='searchbar' ),
    path('', views.home),
    path('add/', views.add_inventory, name='add'),
    path('edit/<int:id>', views.edit_inventory),  
    path('view/<int:id>', views.view_inventory, name='view'),  
    path('<int:id>/update', views.update_inventory, name='update'),  
    path('<int:id>/delete', views.delete_view, name='delete'),  
    path('<int:id>/delete', views.delete_inventory, name='delete_inventory'),  
    path('inventory/', views.InventoryList.as_view()),
    path('<str:sort_order>/', views.home, name='home'),
    path('<str:sort_order>/add', views.add_inventory),
    path('404', views.error_404, name='error_404'),


]