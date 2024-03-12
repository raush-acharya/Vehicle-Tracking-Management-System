from django.db import models

# Create your models here.
class vehicles(models.Model):
    vehicles_name = models.CharField(max_length=50)
    vehicles_description = models.TextField()
    vehicles_seat = models.IntegerField()
    vehicles_door = models.IntegerField()
    vehicles_luggage = models.IntegerField()
    vehicles_price = models.IntegerField()
    vehicles_image=models.FileField(upload_to="vehicles_image/",max_length=250,null=True,default=None)