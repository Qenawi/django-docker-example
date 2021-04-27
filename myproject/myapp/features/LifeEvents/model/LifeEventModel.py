"""
@Docs
"""

from django.db import models

from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


# Description
class LifeEvent(models.Model, AnalyticProtocol):
    life_event_id = models.BigAutoField(primary_key=True)
    life_event_title = models.CharField(max_length=600)
    life_event_date = models.DateTimeField("event Date")
    life_event_success_rate = models.FloatField("Success Rate")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass
