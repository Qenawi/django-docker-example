"""
@Docs
"""

from django.db import models

from myproject.myapp.base.BaseModel import BaseModelProtocol
from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


# Description
class GamingModel(models.Model, AnalyticProtocol, BaseModelProtocol):
    game_id = models.BigAutoField(primary_key=True)
    game_title = models.CharField(max_length=6000)
    game_win_rate = models.FloatField("Success Rate")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass

    def get_hashmap(self):
        result = {
            "id": self.game_id,
            "title": self.game_title,
            "game_success_rate": self.game_win_rate
        }
        return result

        # MARK: insert item

    @staticmethod
    def build_item(dic: dict):
        result = GamingModel(game_title=dic["title"], game_win_rate=dic["game_success_rate"])
        return result

    @staticmethod
    def insert_item(item):
        item: GamingModel
        item.save()

    def __str__(self):
        return self.game_title
