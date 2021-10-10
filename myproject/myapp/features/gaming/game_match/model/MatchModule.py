#   Qenawi created MatchModule.py at 5/17/21, 9:56 AM
#   MatchModule.py @Docs
#

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)
from myproject.myapp.features.gaming.game.model.GamingModel import GamingModel


# Match types wich is going to be included
class MatchType:
    MOBA = "MOBA"
    FBS = "FBS"


# types of champions
class ChampionType:
    # MOBA : League of legend / wild rift /
    MOBA_FIGHTER = "MOBA_FIGHTER"
    MOBA_ASSASSIN = "MOBA_ASSASSIN"
    MOBA_TANK = "MOBA_TANK"
    MOBA_MARK = "MOBA_MARK"
    # FPS : Crossfire / call of duty  /  etc ..
    FPS_Sniper = "FPS_Sniper"
    FPS_Gun = "FPS_Gun"
    FPS_PEWPEW = "FPS_PEWPEW"
    Default = "Default_Champ"


# Description
class MatchModel(models.Model, AnalyticProtocol, BaseModelProtocol):
    # game id  (match) on to many (game)
    match_id = models.BigAutoField(primary_key=True)
    champ_type = models.CharField(max_length=100, default=ChampionType.Default)
    match_win_rate = models.FloatField("Match-Win-Rate", default=0.0)
    game_id = models.ForeignKey('GamingModel', on_delete=models.CASCADE)

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

    def get_hashmap(self):
        result = {
            "game_id": self.game_id,
            "id": self.match_id,
            "champ_type": self.champ_type,
            "match_success_rate": self.match_win_rate
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = MatchModel(game_id=dic["game_id"],
                            champ_type=dic["champ_type"],
                            game_win_rate=dic["match_success_rate"])
        return result

    @staticmethod
    def insert_item(item):
        item: MatchModel
        item.save()

    def __str__(self):
        title = str(self.champ_type) + "%" + str(self.match_win_rate)
        game = GamingModel.objects.get(pk=self.game_id.game_id)
        if game:
            game: GamingModel
            title = game.game_title + "@" + self.champ_type + "%" + str(self.match_win_rate)
        return title
