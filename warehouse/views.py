from django.shortcuts import render, redirect
from warehouse.forms import WarehouseForm


def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_warehouse')
    else:
        form = WarehouseForm()

    return render(request, 'create_warehouse.html', {'form': form})
