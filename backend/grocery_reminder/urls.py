from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('groceries/', views.getGroceries, name='groceries'),
    path('groceries/add/', views.addGrocery, name='add-grocery'),
    # '/grocery/id'
    # /grocery/id/update/
    # /grocery/id/delete/
]