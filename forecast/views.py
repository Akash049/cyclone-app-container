from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers as django_serializers
from django.db.models import Q
from .serializers import *
import math
from .models import *
import csv, json
import os

class FetchLiveForecast(APIView):

    def get(self, request):
        try:
            forecast_array = Forecast.objects.all()
            data = ForecastSerializer(forecast_array, many=True)
            return Response({'result': data.data, 'success': True})
        except Exception as e:
            return Response({'result': repr(e), 'success': False})

class AddForecast(APIView):

    def post(self, request):
        try:
        	name = request.POST.get('name','')
        	cy_id = request.POST.get('cy_id','')
        	cy_name = request.POST.get('cy_name','')
        	image = request.POST.get('test','')
        	forecast = Forecast.objects.create(place_name=name,cyclone_id=cy_id,cyclone_name=cy_name,image_link=image)
        	return Response({'result': forecast.pk, 'success': True})
        except Exception as e:
        	return Response({'result': repr(e), 'success': False})

class DeleteAllForecast(APIView):

    def get(self, request):
        try:
            Forecast.objects.all().delete()
            return Response({'result': 'ALL DATA DELETED', 'success': True})
        except Exception as e:
            return Response({'result': repr(e), 'success': False})