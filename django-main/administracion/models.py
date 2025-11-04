from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    edad = models.PositiveSmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username