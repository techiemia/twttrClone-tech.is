from django.shortcuts import render
from django.http import HttpResponse


def index(render):
    return HttpResponse("Hello World!")
