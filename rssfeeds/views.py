from django.shortcuts import render
from rssfeeds.models import Article

def feed_list(request):
    feeds = Article.objects.all().order_by('-pub_date')  # Assuming you want the newest items first
    return render(request, 'feed_list.html', {'feeds': feeds})