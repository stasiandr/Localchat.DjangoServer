from django.db import models

class ChatPoint(models.Model):
    chat_name = models.CharField(max_length=30)
    x = models.IntegerField()
    y = models.IntegerField()
