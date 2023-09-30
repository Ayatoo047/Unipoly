from django.db import models
from django.contrib.auth.models import User
from base.models import Room

# class DM(models.Model):
#     body = models.TextField(null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     reciever = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name = "reciever")
#     sender = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return self.body[0:50]
    
# class Message(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     body = models.TextField(null=False)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["-updated", '-created']

#     def __str__(self):
#         return self.body[0:50]