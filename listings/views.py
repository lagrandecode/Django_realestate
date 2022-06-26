from django.shortcuts import render
from .models import Listings

# Create your views here.
def listing_list(request):

    listing = Listings.objects.all()
    context = {
        "listing" : listing
    }
    return render(request, 'listings/listing.html', context)
