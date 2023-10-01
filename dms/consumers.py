from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.utils.timesince import timesince
from django.shortcuts import reverse, redirect
from channels.db import database_sync_to_async
# from .models import Statistic
from base.models import Room, Message
from django.contrib.auth.models import User
# from users.models import Profile

class RoomConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_message = None

    async def connect(self):
        # print(self.scope)
        room_name = self.scope['url_route']['kwargs']['slug']

        self.room_name = room_name
        # self.room_name = room_name

        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()
        # print('connection')
 
   
    async def disconnect(self, close_code):
        print('disconnecting', close_code)
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # extramessage = text_data_json['extramessage']
        sender = text_data_json['sender']

        # print(text_data_json['message'], sender)
        room_name = self.room_name

        await self.save_data_item(sender, message, room_name)
        self.new_message = await self.get_new()
        # self.new_messages = await self.get_new()
        # qs = await self.read_data_item(room_name)
        # new_message = self.get_new()

        await self.channel_layer.group_send(self.room_name, {
                'type' : 'statistics_message',
                'message': message,
                'sender': sender,
                # 'create': timesince(new_message['created']),
                # 'user_url': reverse("userprofile", args=[new_message['owner']])
            })

    @database_sync_to_async
    def get_new(self):
        if self.new_message is not None:
            new = Message.objects.filter(id=self.new_message.id).last()
            return {'created': new.created, 'owner': new.user_id}
        else:
            print('nothing dey')
            return {} 
        
    @database_sync_to_async
    def get_new_one(self):
        if self.new_message is not None:
            new = Message.objects.filter(id=self.new_message.id).first()
            return {'created': new.created, 'owner': new.user_id}
        else:
            print('nothing dey again')
            return {} 
        

    async def statistics_message(self, event):
        message = event['message']
        sender = event['sender']
        # print('nothing')
        # print('hhhhhh', new_message)
        # new_message = await self.get_new()
        # print(reverse("userprofile", args=[new_message['owner']]))
        # if self.new_message is None:
        #     print('if is true')
        #     self.new_message = await self.get_new_one()
        #     print("message is his: ", self.new_message)
        #     await self.send(text_data=json.dumps({
        #     'message': message,
        #     'sender': sender,
        #     # 'create': timesince(self.new_message['created']),
        #     # 'user_url': reverse("userprofile", args=[self.new_message['owner']])
        #     }))
        # else:
        try:
            created = timesince(self.new_message['created'])
            user_url = reverse("userprofile", args=[self.new_message['owner']])
        except:
            created = 0
            user_url = 0

        print('else is true')
        print("message is thhhhis: ", self.new_message)
        await self.send(text_data=json.dumps({
        'message': message,
        'sender': sender,
        'create': created,
        'user_url': user_url
        }))
        # print(message, sender)

    @database_sync_to_async
    def create_data_item(self, sender, message, room_name):
        self.new_message = Message.objects.create(
                        user=User.objects.filter(username=sender).first(),
                        body=message,
                        room=Room.objects.filter(slug=room_name).first())
        # print(self.new_message.__dict__)
        return self.new_message
    
    async def save_data_item(self, sender, message, room_name):
        await self.create_data_item(sender, message, room_name)
        # await self.get_new()
        
    @database_sync_to_async
    def read_data_item(self, room_name):
        room = Room.objects.filter(name=room_name).first()
        messages = Message.objects.filter(room=room).all()

        return messages

    # async def show_data_item(self, room_name):
    #     await self.read_data_item(room_name)