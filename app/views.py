# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Function that shows the hello world with an Http Response.
    """
    return HttpResponse("Hello World, This is a Django App that has been deployed on Cloud Foundry 😄")
