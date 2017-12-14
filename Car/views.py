# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Car

# Create your views here.


def takes_index(request, index):
    return HttpResponse(index)


def home_view(request):
    return HttpResponse('<b>CS 361 - SOFTWARE / Homework 1</b>')
