"""
@Docs
"""

import abc

from django.db import models

from myproject.myapp.features.Analytics.protocol.AnalyticProtocol import (
    AnalyticProtocol,
)


class BookModel(models.Model, AnalyticProtocol):
    book_id = models.BigAutoField(primary_key=True)
    book_title = models.CharField(max_length=6000)
    book_start_date = models.DateTimeField("book start reading Date", auto_now_add=True)
    book_end_date = models.DateTimeField("book end reading Date", auto_now_add=True)
    current_page = models.IntegerField("current page")
    page_count = models.IntegerField("current page")

    # MARK:- implement Base Analytic
    def calculate_analytic_value(self):
        pass
