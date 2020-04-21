from django.db import models

# Create your models here.
# class LineCharts(models.Model):
#     xtime = models.TimeField('linetime', null=False)
#     value = models.IntegerField('linevalue', null=False)
#
#     class Meta:
#         db_table = 'linecharts'

class Linecharts(models.Model):
    linetime = models.DateTimeField(blank=True, null=True)
    linevalue = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'linecharts'