from django.core.management.base import BaseCommand
from django.utils import timezone
import feedparser
from rssfeeds.models import RSSFeedItem
from datetime import datetime
import pytz

class Command(BaseCommand):
    help = 'Fetches RSS feed items and stores them in the database'

    def handle(self, *args, **kwargs):
        url = 'http://www.marketwatch.com/rss/StockstoWatch'  # Replace with your RSS feed URL
        d = feedparser.parse(url)

        for entry in d.entries:
            # Convert struct_time to datetime
            pub_date = datetime(*entry.published_parsed[:6], tzinfo=pytz.utc)

            _, created = RSSFeedItem.objects.get_or_create(
                title=entry.title,
                link=entry.link,
                defaults={
                    'description': entry.description,
                    'pub_date': pub_date
                }
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added feed item "{entry.title}"'))
            else:
                self.stdout.write(self.style.WARNING(f'Feed item "{entry.title}" already exists'))