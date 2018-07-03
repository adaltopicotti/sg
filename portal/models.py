from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    ACTIVATE = 1
    DEACTIVATE = 0
    ROLE_CHOICES = (
        (ACTIVATE, 'Ativo'),
        (DEACTIVATE, 'Desativo'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Logo(models.Model):
    titulo = models.CharField(max_length = 200)
    imagem = models.ImageField()

    
class ValidateLogin(models.Model):
    login = models.CharField()
    password = models.CharField()
    token = models.CharField()
    expirate_date = models.DateTimeField()

    def __str__(self):
        return str(self.date)
