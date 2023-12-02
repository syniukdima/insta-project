import json
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model

from chats.models import ChatModel

User = get_user_model()


class PersonalChatConsumer(AsyncWebsocketConsumer):
    """Class for web socket representations for chat"""

    async def connect(self):
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        # називаємо групу від більшого айді користувача до меншого
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name

        # створюємо групу
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.set_online_user(my_id, True)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        # дістаємо json з js
        data = json.loads(text_data)
        message = data['message']

        # перевіряємо повідомлення на пустоту
        if message.strip() != "":
            username = data['username']
            my_time = datetime.now()

            new_day = False
            if await self.get_last_date(self.room_group_name):
                last_date = await self.get_last_date(self.room_group_name)

                my_time_year = my_time.year
                my_time_day = my_time.day
                last_date_year = last_date.timestamp.year
                last_date_day = last_date.timestamp.day

                diffetence_day = False
                if my_time_year >= last_date_year and my_time_day > last_date_day:
                    diffetence_day = True

                if diffetence_day:
                    new_day = True
            else:
                new_day = True
            # перевіряємо чи є в повідомленні голосове
            if data['base64'] == "1":
                await self.save_message(
                    username, self.room_group_name, message, my_time, True, new_day)
            else:
                await self.save_message(
                    username, self.room_group_name, message, my_time, False, new_day)
            # відправка даних в chat_message
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'username': username,
                    'timestamp': my_time,
                    'base64': data['base64'],
                    'new_day': new_day,
                }
            )

    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        base64 = event['base64']
        new_day = event['new_day']

        # відправка даних в json, для подальшої роботи в js
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'base64': base64,
            'new_day': new_day,
        }))

    async def disconnect(self, code):
        my_id = self.scope['user'].id
        await self.set_online_user(my_id, False)
        await self.set_last_time_online(my_id)
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # збереження повідомлення в базі даних
    @database_sync_to_async
    def save_message(self, username, thread_name, message, my_time, base=False, new_day=False):
        ChatModel.objects.create(
            sender=username, message=message, thread_name=thread_name,
            timestamp=my_time, base64=base, new_day=new_day)

    @database_sync_to_async
    def set_online_user(self, id, data):
        User.objects.filter(id=id).update(is_online=data)

    @database_sync_to_async
    def set_last_time_online(self, id):
        User.objects.filter(id=id).update(last_time_online=datetime.now())

    @database_sync_to_async
    def get_last_date(self, thread_name):
        return ChatModel.objects.filter(thread_name=thread_name).last()
