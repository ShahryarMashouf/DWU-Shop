from django.db import models

class Packages(models.Model):
    name = models.CharField(max_length= 255)
    price = models.FloatField()
    description = models.CharField(max_length=600, default="Default description")
    image_url = models.CharField(max_length=2083)
    
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    discount = models.FloatField()