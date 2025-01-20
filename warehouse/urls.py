from django.contrib.auth.views import LoginView
from django.urls import path

from warehouse.views import create_warehouse

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('create/', create_warehouse, name='create_warehouse'),

]