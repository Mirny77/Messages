# coding=utf-8
from django.conf.urls import url,include
from chat_room.views import *

urlpatterns = [
    url(r'^room/$', Rooms.as_view()),
    url(r'^dialog/$', Dialog.as_view()),
]