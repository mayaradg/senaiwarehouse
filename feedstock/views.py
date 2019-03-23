from django.shortcuts import render
from .models import Feedstock
from address.models import FeedstockAdress

# Create your views here.

def feedstock_list(request):
    feedstocks = Feedstock.objects.all()
    return render(request, 'feedstock/feedstock_list.html', {'feedstocks':feedstocks})

def get_address(request, pk):
    addresses = FeedstockAdress.objects.filter(feedstock__pk=pk)
    return render(request, 'feedstock/address.html', {'addresses':addresses})
