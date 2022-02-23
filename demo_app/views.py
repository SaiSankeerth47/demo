from asyncio.windows_events import NULL
import csv
from datetime import date
# from genericpath import exists
from django.shortcuts import render
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from demo.settings import *
from django.core.files.storage import FileSystemStorage
import os
#import pandas as pd
import datetime
import calendar


class index(APIView):
    
    
    def post(self,request):
        name=request.data['student']
        return Response('post')
    def get(self,request):
        return HttpResponse('get sankeerth')