from django.db.models import signals
from .models import UserMemeberShip, Memebership, 

def post_save_user_membership(sender, instance,created, *args, **kwargs):
    if created:
        UserMemeberShip.objects.get_or_create(user=instance)
    user_membership, created = UserMemeberShip.objects.get_or_create(user=instance)
    