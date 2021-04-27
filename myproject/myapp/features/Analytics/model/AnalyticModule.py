"""
@Docs
"""

from django.db import models


# Description
class AnalyticModule(models.Model):
    analytic_id = models.BigAutoField(primary_key=True)
    analytic_title = models.CharField("analytic title", max_length=6000)
    analytic_date = models.DateTimeField("analytic Date", auto_now_add=True)
    analytic_amount = models.FloatField("analytic Amount")
