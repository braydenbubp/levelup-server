from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=100)
    maker = models.CharField(max_length=50)
    number_of_players = models.IntegerField(default=0)
    skill_level = models.IntegerField(default=0)
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
