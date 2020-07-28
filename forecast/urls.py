from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^all/$', FetchLiveForecast.as_view(), name='GET ALL FORECAST TILL NOW'), 
    url(r'^add/$', AddForecast.as_view(), name='ADD NEW FORECAST'), 
    url(r'^delete_all/$', DeleteAllForecast.as_view(), name='DELETE ALL FORECAST'), 
]