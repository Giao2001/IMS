from django.contrib import messages
from django.shortcuts import render, redirect
from warehouse.forms import WarehouseForm


def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Warehouse created successfully!')
            form = WarehouseForm()
    else:
        form = WarehouseForm()

    return render(request, 'create_warehouse.html', {'form': form})
