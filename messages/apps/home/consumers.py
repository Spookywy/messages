import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = "main_group"
        # Join group
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        # Tell other users a new one joined the channel
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat_info",
                "info": "{} joined the channel.".format(self.scope["user"].username),
            },
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat_info",
                "info": "{} left the channel.".format(self.scope["user"].username),
            },
        )

        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                "type": "chat_message",
                "message": message,
                "message_sender": self.scope["user"].username,
            },
        )

    def chat_message(self, event):
        message = event["message"]
        message_sender = event["message_sender"]

        # Send message to WebSocket
        self.send(
            text_data=json.dumps({"message_sender": message_sender, "message": message})
        )

    def chat_info(self, event):
        info = event["info"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"info": info}))
