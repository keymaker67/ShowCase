from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Record
from .forms import AddCustomerForm


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        records = Record.objects.all()
        return render(request, 'main/home.html', {'records': records})
    else:
        return render(request, 'main/home.html', {})


def customer_detail_view(request, pk):
    if request.user.is_authenticated:
        customer_detail = Record.objects.get(id=pk)
        return render(request, 'main/customer_detail.html', {'customer_detail': customer_detail})
    else:
        messages.success(request, 'You should be logged in first!')
        return redirect('home')


def customer_delete_view(request, pk):
    if request.user.is_authenticated:
        customer_delete = Record.objects.get(id=pk)
        customer_delete.delete()
        messages.success(request, f'customer {customer_delete} deleted successfully.')
        return redirect('home')
    else:
        messages.success(request, 'You should be logged in first!')
        return redirect('home')


def customer_add_view(request):
    if request.user.is_authenticated:
        form = AddCustomerForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                customer = form.save()
                messages.success(request, f'customer {customer} added successfully.')
                return redirect('customer_add')
            else:
                messages.success(request, 'form was not valid!')
                return redirect('customer_add/')
        else:
            return render(request, 'main/customer_add.html', {'form': form})
    else:
        messages.success(request, 'You should be logged in first!')
        return redirect('home')


def customer_update_view(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                customer = form.save()
                messages.success(request, f'customer {customer} added successfully.')
                return redirect('home')
            else:
                messages.success(request, 'form was not valid!')
                return redirect('customer_update/')
        else:
            return render(request, 'main/customer_update.html', {'form': form})
    else:
        messages.success(request, 'You should be logged in first!')
        return redirect('home')
