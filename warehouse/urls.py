from django.urls import path

from warehouse.views import create_warehouse

urlpatterns = [
    path('create/', create_warehouse, name='create_warehouse'),
]