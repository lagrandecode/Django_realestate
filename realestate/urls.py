
from django.contrib import admin
from django.urls import path
from listings.views import (
    listing_list, 
    listing_retrieve, 
    listing_create, 
    listing_update
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listing/<pk>/', listing_retrieve),
    path('listing/<pk>/edit/', listing_update),
    path('add/', listing_create)
]
