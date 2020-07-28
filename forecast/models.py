from django.db import models
from django.utils import timezone
from datetime import datetime

class Forecast(models.Model):
	place_name = models.CharField(max_length=150,null=False,blank=False)
	cyclone_id = models.CharField(max_length=10,null=True,blank=True)
	cyclone_name = models.CharField(max_length=200,blank=True, null=True)
	image_link = models.CharField(max_length=500,blank=True, null=True)
	time_of_last_forecast = models.DateTimeField(default=datetime.now)
	created_at = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.place_name 