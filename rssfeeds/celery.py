# In rssfeeds/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rssfeeds.settings')

app = Celery('rssfeeds')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# In rssfeeds/celery.py (add this to the existing configuration)

from celery.schedules import crontab

app.conf.beat_schedule = {
    'run_my_command_every_30_seconds': {
        'task': 'rssfeeds.tasks.rssfeeds',
        'schedule': 30.0,  # seconds
    },
}
