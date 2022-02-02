import json
from unicodedata import name
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.exceptions import StopConsumer
import datetime
from datetime import timezone
from hksfbclone.models import Chat, Chat_Groups,User
from channels.db import database_sync_to_async

class MyASyncConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        self.group_name=self.scope['url_route']['kwargs']['groupname']
        print('websocket connected..')
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
    
    async def receive(self,text_data=None,bytes_data=None):
        print('message recived succesfully...',text_data)
        data=json.loads(text_data)
        message=data['msg']
        group1=await database_sync_to_async(Chat_Groups.objects.get)(name=self.group_name)
        user=await database_sync_to_async(User)(username=self.scope["user"].username)
        chat=Chat(
            user=self.scope["user"],
            group=group1,
            message=data['msg'],
            timestamp=datetime.datetime.now(timezone.utc)
        )
        await database_sync_to_async(chat.save)()
        await self.channel_layer.group_send(
            self.group_name,
            {
            'type':'chat.message',
            'message': message
            }
        )
    async def chat_message(self,event):
        await self.send(text_data=json.dumps({
            'msg':event['message']
        }))
    async def disconnect(self,event):
        print('websocket disconnected...',event)
        self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer