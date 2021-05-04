from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30, blank=True)
    apellidos = models.CharField(max_length=30, blank=True)
    #
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos

    def get_absolute_url(self):
        return reverse('usuarios_app:user-login')

    class Meta:
        ordering = ('-last_login',)