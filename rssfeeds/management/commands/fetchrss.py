from django.core.management.base import BaseCommand
from rssfeeds.models import RSSFeedItem
import feedparser
from datetime import datetime
import pytz

class Command(BaseCommand):
    help = 'Fetches and parses an RSS feed and stores it in the database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to fetch and parse the RSS feed...")
        feed_url = 'https://www.investing.com/rss/stock_stock_picks.rss'  # Replace with your feed URL

        feed = feedparser.parse(feed_url)
        if feed.bozo:
            self.stdout.write(f"Error parsing feed: {feed.bozo_exception}")
            return

        for entry in feed.entries:
            pub_date = self.parse_date(entry.get('published_parsed'))

            # Create a new RSSFeedItem or update existing one
            rss_item, created = RSSFeedItem.objects.update_or_create(
                link=entry.get('link', '#'),
                defaults={
                    'title': entry.get('title', 'No Title'),
                    'pub_date': pub_date,
                    'author': entry.get('author', 'Unknown Author'),
                    'description': entry.get('description', 'No Description')
                }
            )

            if created:
                self.stdout.write(f'Added new RSS feed item: {rss_item.title}')
            else:
                self.stdout.write(f'Updated existing RSS feed item: {rss_item.title}')

    def parse_date(self, published_parsed):
        if published_parsed:
            return datetime(*published_parsed[:6], tzinfo=pytz.utc)
        return None