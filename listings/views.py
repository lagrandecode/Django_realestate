from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Listings
from .form import CreatListForm

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


#view for form 

def listing_create(request):
    form = CreatListForm()
    if request.method == "POST":
        form = CreatListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, 'createform.html', context)



def listing_update(request, pk):
    listingUpdate = Listings.objects.get(id=pk)
    form = CreatListForm(instance=listingUpdate)

    if request.method == "POST":
        form = CreatListForm(request.POST, instance=listingUpdate)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        "form" : form
    }
    return render(request, 'listing_update.html', context)

