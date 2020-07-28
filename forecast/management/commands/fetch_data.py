from datetime import timedelta, time, datetime
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
import requests, re
from bs4 import BeautifulSoup
from forecast.models import *

today = timezone.now()
tomorrow = today + timedelta(1)
today_start = make_aware(datetime.combine(today, time()))
today_end = make_aware(datetime.combine(tomorrow, time()))

URL = 'http://rammb.cira.colostate.edu/products/tc_realtime/index.asp'
FORECAST_TABLE_PREFIX_URL = "http://rammb-data.cira.colostate.edu/tc_realtime/%s"
IMAGE_URL_PREFIX = "https://rammb-data.cira.colostate.edu/%s"

class Command(BaseCommand):
    help = "This Function scraps the cyclone data from website"

    def handle(self, *args, **options):
    	page = requests.get(URL)
    	results = BeautifulSoup(page.content, 'html.parser')
    	cyclon_result_array = results.find_all('div', class_='basin_storms')
    	for place_item in cyclon_result_array:
    		place_block = place_item.find('h3')
    		_place_name = place_block.text

    		cyclone_ul_list = place_item.find('ul')
    		cyclone_li_items = cyclone_ul_list.find_all('li')
    		for cyclone in cyclone_li_items:
    			if cyclone.text == 'No Currently Active Cyclones':
    				# Update the data to table
    				forecast = Forecast.objects.create(place_name=_place_name)
    			else:
    				_cyclone_id = cyclone.text.split("-")[0].strip()
    				_cyclone_name = cyclone.text.split("-")[1].strip()
    				forecast_a_tag = cyclone.find('a')
    				forecast_img_tag = forecast_a_tag.find('img')
    				forecast_link = forecast_a_tag.get("href")
    				forecast_gif_link = forecast_img_tag.get("src")
    				_forecast_table_link = FORECAST_TABLE_PREFIX_URL % (forecast_link)
    				_forecast_gif_url = IMAGE_URL_PREFIX % (forecast_gif_link)
    				# Update the data to table
    				forecast = Forecast.objects.create(place_name=_place_name,cyclone_id=_cyclone_id,cyclone_name=_cyclone_name,image_link=_forecast_gif_url)
