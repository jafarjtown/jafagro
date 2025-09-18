from django.db import models

# Create your models here.

class Item(models.Model):
  name = models.CharField(max_length=255)
  price = models.IntegerField(default=500)
  weight = models.FloatField()
  image = models.FileField(upload_to='images')
  
class Order(models.Model):
  name = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  address = models.TextField()
  quantity = models.IntegerField(default=5)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  