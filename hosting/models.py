from django.db import models

# Create your models here.
class Room(models.Model):
    image =models.URLField(max_length=200)
    name =models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=25)
    price = models.FloatField()
    occupied = models.BooleanField(default=False)
    is_cleaned = models.BooleanField()
    
    def __str__(self):
        return self.name 
class Client(models.Model):
    contact= models.IntegerField()
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    duration = models.DateField(auto_now=False, auto_now_add=False)
    begin = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.room

class Review(models.Model):
    description = models.TextField()
    user= models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
