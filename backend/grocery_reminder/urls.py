from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('groceries/', views.getGroceries, name='groceries'),
    path('groceries/add/', views.addGrocery, name='add-grocery'),
    path('groceries/<str:pk>', views.getGrocery, name="Get Grocery item"),
    path('groceries/<str:pk>/update/', views.updateGrocery, name="update grocery"),
    path('groceries/<str:pk>/delete/', views.deleteGrocery, name="delete grocery"),
]