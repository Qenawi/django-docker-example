from django.db import models

from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import AnalyticProtocol


class BudgetModel(models.Model, AnalyticProtocol):
    budget_id = models.BigAutoField(primary_key=True)
    budget_title = models.CharField("budget title", max_length=6000)
    budge_date = models.DateTimeField("budget Date", auto_now_add=True)
    budget_amount = models.FloatField("budget Amount")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass
