# In rssfeeds/__init__.py
from __future__ import absolute_import, unicode_literals
from .celery import app as rssfeeds

__all__ = ('rssfeeds',)