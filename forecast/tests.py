from django.test import TestCase
from forecast.models import Forecast
from django.utils import timezone
from django.core.urlresolvers import reverse

# Testing the DB setup
class DataUpdateTest(TestCase):

    def create_forecast(self, place_name="Sanmple Place"):
        return Forecast.objects.create(place_name=place_name)

    def test_create_forecast(self):
        w = self.create_forecast()
        self.assertTrue(isinstance(w, Forecast))
        self.assertEqual(w.__unicode__(), w.place_name)

class PreventDataAddWithoutPlaceNameTest(TestCase):

    def create_forecast(self, cyclone_name="Sample Name"):
    	try:
    		Forecast.objects.create(cyclone_name=cyclone_name)
        except Exception as e:
        	print(repr(e)) 

    def test_mandatory_name(self):
    	forecast_filter = Forecast.objects.filter(cyclone_name=cyclone_name)
        self.assertEqual(forecast_filter.exists(), False)

