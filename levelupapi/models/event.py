from django.db import models
from .gamer import Gamer
from .game import Game

class Event(models.Model):
    description = models.CharField(max_length=100)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    @property
    def joined(self):
        return self.__joined
    
    @joined.setter
    def joined(self, value):
        self.__joined = value
