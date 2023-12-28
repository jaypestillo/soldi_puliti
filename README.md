# GitHub RSSFeeds

This is a Django project. 

## Django Related 

```python
python3 manage.py collectstatic
```
To run this application:

```python
python3 manage.py runserver
```

## RabbitMQ Server

You can start the RabbitMQ server using the following command:
```python
rabbitmq-server

```
Or, to run it as a background service:
```python
brew services start rabbitmq

```
RabbitMQ comes with a management console, which provides a user-friendly UI to manage and monitor your RabbitMQ server. You can enable it with the following command:
```python
rabbitmq-plugins enable rabbitmq_management

```
After enabling, you can access the management console through your browser at http://localhost:15672/. The default username and password are both guest

Once RabbitMQ is running, integrate it with your Django project as the broker for Celery. Update your Django project's settings to use RabbitMQ:
```python
CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

```
This configuration uses the default RabbitMQ user (guest), which is sufficient for development purposes.

## Celery app

In your Django project (same level as settings.py), create a file named celery.py to define your Celery app:
```python
# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')

app = Celery('your_project_name')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


```
Replace your_project_name with the name of your Django project.

In your project's __init__.py file, import the Celery application:
```python
# __init__.py

from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)


```
Finally, to start processing tasks, run the Celery worker:
```
celery -A your_project_name worker -l info
```

Run the following to watch workers running in your celery app:

```
celery -A rssfeeds worker --loglevel=info
```
Run the following to watch beats for your celery app:

```
celery -A rssfeeds beat -l info
```

## Data related commands

```python
python3 manage.py shell
```