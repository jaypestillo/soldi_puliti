from django.shortcuts import render
from .models import RSSFeedItem

def feed_list(request):
    feeds = RSSFeedItem.objects.all().order_by('-pub_date')  # Assuming you want the newest items first
    return render(request, 'feed_list.html', {'feeds': feeds})