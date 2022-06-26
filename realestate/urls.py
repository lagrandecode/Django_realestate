
from django.contrib import admin
from django.urls import path
from listings.views import listing_list, listing_retrieve
from listings.views import listing_create


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listing/<pk>/', listing_retrieve),
    path('add/', listing_create)
]
