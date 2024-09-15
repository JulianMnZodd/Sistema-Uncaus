from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cama
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Cama)
def cama_post_save(sender, instance, **kwargs):
    logger.debug(f"Signal disparado por Cama ID={instance.idcama}")

    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "camas_group",
        {
            "type": "send_cama_update",
            "idcama": instance.idcama,
            "estado": instance.estado,
            "paciente": instance.paciente.idpaciente.nombre if instance.paciente else 'Libre',
        }
    )
