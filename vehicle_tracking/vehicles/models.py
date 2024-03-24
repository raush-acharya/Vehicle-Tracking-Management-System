from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class vehicles(models.Model):
    vehicles_name = models.CharField(max_length=50)
    vehicles_description = models.TextField()
    vehicles_seat = models.IntegerField()
    vehicles_door = models.IntegerField()
    vehicles_luggage = models.IntegerField()
    vehicles_price = models.DecimalField(max_digits=10, decimal_places=2)
    vehicles_image=models.FileField(upload_to="vehicles_image/",max_length=250,null=True,default=None)

class Booking(models.Model):
    vehicle = models.ForeignKey(vehicles, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)