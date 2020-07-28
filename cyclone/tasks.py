from celery import shared_task
from django.core.management import call_command

@shared_task
def fetch_data_task():
	call_command("fetch_data", )
	print("Initiated the fetch request.")