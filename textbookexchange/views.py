from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.views import serve
import os

def index(request):
    
    return HttpResponse("B-30 Club")