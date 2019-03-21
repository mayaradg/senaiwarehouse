from django.shortcuts import render
from .models import Feedstock

# Create your views here.

def feedstock_list(request):
    feedstocks = Feedstock.objects.all()
    return render(request, 'feedstock/feedstock_list.html', {'feedstocks':feedstocks})

def get_address(request, pk):
    address = Feedstock.objects.get(id=pk).address
    return render(request, 'feedstock/address.html', {'address':address})
