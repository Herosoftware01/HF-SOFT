# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async
# from django.core.serializers.json import DjangoJSONEncoder  # ✅ Import this
# from .models import TBuyer

# class FabricConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         await self.send_data()

#     @sync_to_async
#     def get_data(self):
#         print("received connections")
#         return list(TBuyer.objects.using('testing').values())

#     async def send_data(self):
#         data = await self.get_data()
#         await self.send(text_data=json.dumps({
#             'type': 'initial',
#             'data': data
#         }, cls=DjangoJSONEncoder))  # ✅ Fix: This handles date serialization

#     async def receive(self, text_data):
#         pass


import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import TBuyer
from datetime import date

class FabricConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("fabric_updates", self.channel_name)
        await self.send_initial_data()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("fabric_updates", self.channel_name)

    @sync_to_async
    def get_all_buyers(self):
        # Use your db alias if needed, else remove .using()
        qs = list(TBuyer.objects.using('testing').all().values())
        # Convert date fields to string for JSON serialization
        for d in qs:
            if d.get('date') and isinstance(d['date'], date):
                d['date'] = d['date'].isoformat()
        return qs

    async def send_initial_data(self):
        data = await self.get_all_buyers()
        await self.send(text_data=json.dumps({
            'type': 'initial',
            'data': data
        }))

    # Handler for messages sent to the group (new buyer)
    async def new_buyer(self, event):
        buyer_data = event['data']
        # Make sure date is serialized as string
        if buyer_data.get('date') and isinstance(buyer_data['date'], date):
            buyer_data['date'] = buyer_data['date'].isoformat()
        await self.send(text_data=json.dumps({
            'type': 'new_buyer',
            'data': buyer_data
        }))

def serialize_tbuyer(instance):
    return {
        'buyerid': instance.buyerid,
        'buyername': instance.buyername,
        'orderno': instance.orderno,
        'date': instance.date.isoformat() if instance.date else '',
        'guid': instance.guid,
        'refresh': instance.refresh,
    }