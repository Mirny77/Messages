from django.db import models

from django.contrib.auth.models import User



class Room(models.Model):
    
    creater = models.ForeignKey(User, verbose_name="Создатель")
    invited = models.ManyToManyField(User, verbose_name="Участники")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Комната чата"
        verbose_name_plural = "Комнаты чатов"


class Chat(models.Model):
    
    room = models.ForeignKey(Room, verbose_name="Комната чата")
    user = models.ForeignKey(User, verbose_name="Пользователь")
    text = models.TextField("Сообщение", max_length=500)
    date = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение чата"
        verbose_name_plural = "Сообщения чатов"

