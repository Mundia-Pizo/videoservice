from django.db.models.signals import post_save
from .models import UserMemberShip, Membership, 
from django.contrib.auth import settings

def post_save_user_membership(sender, instance,created, *args, **kwargs):
    if created:
        UserMemberShip.objects.get_or_create(user=instance)
    user_membership, created = UserMemberShip.objects.get_or_create(user=instance)
    #where we will put the user connectio to the membership
    user_membership.save()
    
post_save.connect(post_save_user_membership, sender=settings.AUTH_USER_MODEL)