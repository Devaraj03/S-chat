# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.db import database_sync_to_async
# from django.contrib.auth.models import User
# from .models import Message


# class ChatConsumer(AsyncWebsocketConsumer):

#     async def connect(self):

#         self.other_user_id = self.scope["url_route"]["kwargs"]["user_id"]

#         self.user = self.scope["user"]

#         if not self.user.is_authenticated:
#             await self.close()
#             return

#         users = sorted([
#             str(self.user.id),
#             str(self.other_user_id)
#         ])

#         self.room_name = f"chat_{users[0]}_{users[1]}"

#         await self.channel_layer.group_add(
#             self.room_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def disconnect(self, close_code):

#         await self.channel_layer.group_discard(
#             self.room_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):

#         data = json.loads(text_data)

#         message = data["message"]

#         await self.save_message(
#             self.user.id,
#             self.other_user_id,
#             message
#         )

#         await self.channel_layer.group_send(
#             self.room_name,
#             {
#                 "type": "chat_message",
#                 "sender": self.user.username,
#                 "message": message
#             }
#         )

#     async def chat_message(self, event):

#         await self.send(
#             text_data=json.dumps({
#                 "sender": event["sender"],
#                 "message": event["message"]
#             })
#         )

#     @database_sync_to_async
#     def save_message(
#         self,
#         sender_id,
#         receiver_id,
#         content
#     ):
#         sender = User.objects.get(id=sender_id)

#         receiver = User.objects.get(id=receiver_id)

#         Message.objects.create(
#             sender=sender,
#             receiver=receiver,
#             content=content
#         )