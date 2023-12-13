from django.db import models

class RSSFeedItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    category = models.TextField()
    source = models.TextField()
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100, blank=True, null=True)
    # Additional fields depending on your requirements:
    # category = models.CharField(max_length=100, blank=True, null=True)
    # guid = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title
