from django.db import models
from django.contrib.auth import settings
from django.db.models.signals import post_save

CHOICES=(
    ( 'Professional', 'pro'),
    ( 'Enterprise', 'ent'),
    ('Free','free')
)

class Membership(models.Model):
    slug   = models.SlugField()
    membership_type = models.CharField(max_length=52, choices=CHOICES, default='free')
    price  = models.FloatField()

    def __str__(self):
        return self.membership_type

class UserMemberShip(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

def post_save_user_membership(sender, instance,created, *args, **kwargs):
    if created:
        UserMemberShip.objects.get_or_create(user=instance)
    user_membership, created = UserMemberShip.objects.get_or_create(user=instance)
    #where we will put the user connectio to the membership
    user_membership.save()
    
post_save.connect(post_save_user_membership, sender=settings.AUTH_USER_MODEL)

class Subscription(models.Model):
    user_membership=models.ForeignKey(UserMemberShip, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.user_membership.user.username


class Payments(models.Model):
    user   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.FloatField()
    tx_ref = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} Paymemt"



        
    

    


