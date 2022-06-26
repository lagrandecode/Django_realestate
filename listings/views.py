from unicodedata import name
from django.shortcuts import render
from .models import Listings

# Create your views here.
def listing_list(request):

    listing = Listings.objects.all()
    context = {
        "listing" : listing
    }
    return render(request, 'listings/listing.html', context)

# This function is used to retrieve the object from the admin 
def listing_retrieve(request, pk):
    retrieve = Listings.objects.get(id=pk)
    context = {
        "retrieve" : retrieve
    }
    return render(request, 'listings/retrieve.html', context)

