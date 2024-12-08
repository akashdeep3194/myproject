from channels.generic.websocket import AsyncWebsocketConsumer
import json

class AuctionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "auction_room",
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "auction_room",
            self.channel_name
        )

    async def receive(self, text_data):
        print("Message has been received !")
        print(self.scope)
        import ipdb; ipdb.set_trace()
        bid_data=json.loads(text_data)
        amount = bid_data.get('x')
        # # Broadcast bid to all members in the auction room
        await self.channel_layer.group_send(
            "auction_room",
            {
                "type": "auction_message",
                "bid": amount
            }
        )
        self.auction_message(
            {
                "type": "auction_message",
                "bid": amount
            }
        )

    async def auction_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'bid': event['bid']
        }))
