# Generated by Django 3.2 on 2021-04-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_budgetmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AnalyticModule",
            fields=[
                ("analytic_id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "analytic_title",
                    models.CharField(max_length=6000, verbose_name="analytic title"),
                ),
                (
                    "analytic_date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="analytic Date"
                    ),
                ),
                ("analytic_amount", models.FloatField(verbose_name="analytic Amount")),
            ],
        ),
    ]
