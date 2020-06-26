from django.db import models
from django.contrib.auth import settings

CHOICES=(
    ('pro', 'professional'),
    ('ent', 'enterprise'),
    ('free', 'free')
)

class Memebership(models.Model):
    slug   = models.SlugField()
    membership_type = models.CharField(max_length=4, choices=CHOICES, default='free')
    price  = models.FloatField()

    def __str__(self):
        return self.membership_type

class UserMemeberShip(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membership = models.ForeignKey(Memebership, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Subscription(models.Model):
    user_membership=models.ForeignKey(UserMemeberShip, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.user_membership.user.username

    
    


