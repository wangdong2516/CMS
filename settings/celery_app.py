import os
from celery import Celery

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.pro_settings')


app = Celery('CMS')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()