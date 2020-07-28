from rest_framework import serializers
from .models import *

class ForecastSerializer(serializers.ModelSerializer):
    class Meta():
        model = Forecast
        fields = ('place_name','cyclone_id','cyclone_name','image_link','time_of_last_forecast','created_at')