from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from django.conf import settings
from agents.models import Agents

@receiver(post_save,sender = settings.AUTH_USER_MODEL)
def create_agent_account(sender,**kwargs):
    if kwargs['created']:
        agent = Agents.objects.create(user=settings.AUTH_USER_MODEL)
        