from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField()
    capacity = models.IntegerField()
    location = models.TextField()
    
    def __str__(self):
        return f"Room #{self.number} - capacity - {self.capacity}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings") # CASCADE deletes all child classes 
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    creation_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["starttime"]