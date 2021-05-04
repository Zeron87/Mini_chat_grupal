from django.db import models

from users.models import User

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='messages_chat', blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('datetime',)
