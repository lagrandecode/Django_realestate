

from django.db import models

# Create your models here.

class Listings(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    house_no = models.IntegerField()
    square_metre = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.title

   

 
