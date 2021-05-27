from django.db import models


# Create your models here.

class School(models.Model):
    sc_name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Назва школи")
    sc_manager = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name="Директор")
    sc_address = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Адреса школи")
    sc_site = models.CharField(max_length=60, blank=True, null=True, default=None, verbose_name="Сайт школи")
    sc_phone = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Номер телефону")
    sc_lon = models.FloatField(verbose_name="Довгота")
    sc_lat = models.FloatField(verbose_name="Широта")


class University(models.Model):
    un_name = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Назва університету")
    un_manager = models.CharField(max_length=50, blank=True, null=True, default=None, verbose_name="Ректор")
    un_address = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Адреса університету")
    un_site = models.CharField(max_length=60, blank=True, null=True, default=None, verbose_name="Сайт університету")
    un_phone = models.CharField(max_length=100, blank=True, null=True, default=None, verbose_name="Номер телефону")
    un_lon = models.FloatField(verbose_name="Довгота")
    un_lat = models.FloatField(verbose_name="Широта")
