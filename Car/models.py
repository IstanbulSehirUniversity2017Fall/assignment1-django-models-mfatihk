# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Model(models.Model):
    model = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)

    def __str__(self):
        return self.engine

# Create your models here.
