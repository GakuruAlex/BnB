from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    image =models.ImageField(upload_to='images/')
    name =models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=25)
    price = models.FloatField()
    occupied = models.BooleanField(default=False)
    is_cleaned = models.BooleanField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.name 
class Client(models.Model):
    contact= models.IntegerField()
    name = models.ForeignKey(User,on_delete=models.CASCADE,default=1 )
    
    client = None  # client field should be set after saving the object

    def __str__(self):
        return self.name.username  # return the username of the related User object

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.client = self.name.id  # set the client field to the id of the related User object
        super().save(*args, **kwargs) 
        # save the object again to update the client field
class Booking(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    duration = models.IntegerField()
    begin = models.DateField(auto_now=False, auto_now_add=False)
    end = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.room
    
    class Meta:
        ordering =['room','begin']

class Review(models.Model):
    description = models.TextField()
    user= models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
