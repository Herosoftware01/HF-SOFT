from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import TBuyer
from .utils import serialize_tbuyer  # import from utils now

@receiver(post_save, sender=TBuyer)
def send_new_buyer_data(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        data = serialize_tbuyer(instance)
        async_to_sync(channel_layer.group_send)(
            'buyers_group',
            {
                'type': 'new_buyer',
                'message': data,
            }
        )
