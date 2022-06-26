from dataclasses import field
from statistics import mode
from django.forms import ModelForm
from .models import Listings

class CreatListForm(ModelForm):
    class Meta:
        model = Listings 
        fields = [
            'title',
            'price',
            'house_no', 
            'square_metre', 
            'description', 
            'address']
