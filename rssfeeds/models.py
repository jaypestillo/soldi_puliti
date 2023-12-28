from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    author = models.CharField(max_length=100, blank=True, null=True)
    link = models.URLField()
    content = models.TextField(blank=True, null=True)  # Field for article content

    def __str__(self):
        return self.title
