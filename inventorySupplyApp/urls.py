from django.urls import path,re_path    
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add_inventory),
    path('edit/<int:id>', views.edit_inventory),  
    path('view/<int:id>', views.view_inventory),  
    path('<int:id>/update', views.update_inventory),  
    path('<int:id>/delete', views.delete_inventory),  
    path('inventory/', views.InventoryList.as_view()),
     path('', views.home_sort_by_type, name='home_sort_by_type'),
     path('', views.home_sort_by_loc, name='home_sort_by_loc'),
    re_path(r'^filter/(?P<letter>[A-Z])/$', views.home, name='filter_letter')

]