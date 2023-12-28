from django.core.management.base import BaseCommand
import requests
import feedparser
from datetime import datetime
import pytz
from bs4 import BeautifulSoup
from rssfeeds.models import Article  # Adjust this import to your project structure

class Command(BaseCommand):
    help = 'Fetches RSS feeds and stores them in the database'

    def handle(self, *args, **options):
        rss_url = 'https://www.investing.com/rss/news_25.rss'
        self.fetch_and_store_rss(rss_url)

    def scrape_article_content(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # Adjust the selector according to the structure of the web page
            content = soup.find('div', class_='article-content').get_text(strip=True)
            return content
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error scraping article content: {e}"))
            return ""

    def fetch_and_store_rss(self, url):
        response = requests.get(url)
        raw_data = response.text

        feed = feedparser.parse(raw_data)

        for entry in feed.entries:
            title = entry.title
            link = entry.link
            author = entry.get('author', '')

            if entry.published_parsed:
                pub_date = datetime(*entry.published_parsed[:6])
                pub_date = pytz.utc.localize(pub_date)
            else:
                continue

            content = self.scrape_article_content(link)

            if not Article.objects.filter(link=link).exists():
                article = Article(title=title, pub_date=pub_date, author=author, link=link, content=content)
                article.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully saved article: {title}'))