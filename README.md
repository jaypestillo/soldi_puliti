# GitHub RSSFeeds

Welcome to your shiny new Codespace running Django! We've got everything fired up and running for you to explore Django.

You've got a blank canvas to work on from a git perspective as well. There's a single initial commit with the what you're seeing right now - where you go from here is up to you!

```python
python manage.py collectstatic
```
To run this application:

```python
python manage.py runserver
```

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
```python
celery -A your_project_name worker -l info

```