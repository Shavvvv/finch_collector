from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('finches/', views.finches_index, name='finches'),
 path('finches/<int:finch_id>/', views.finches_detail, name='detail'),

 path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),

# Add the new routes below
path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finches_update'),
path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finches_delete'),
path('finches/<int:finch_id>/add_insurance/', views.add_insurance, name='add_insurance'),
path('finches/<int:finch_id>/assoc_food/<int:food_id>/', views.assoc_food, name='assoc_food'),
path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
 path('foods/<int:pk>/', views.FoodDetail.as_view(), name='foods_detail'),
 path('Foods/<int:pk>/delete/', views.FoodDelete.as_view(), name='foods_delete'),


]
