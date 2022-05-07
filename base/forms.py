from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

# class MessageForm(ModelForm):
#     class Meta:
#         model = Message
#         fields = ['body']