from django.db import models

class RSSFeedItem(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    pub_date = models.DateTimeField(null=True, blank=True)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
