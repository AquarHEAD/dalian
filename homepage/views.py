from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from random import choice
from dalian.categories.models import Category
from dalian.quotes.models import Quote
from dalian.settings import LOGIN_KEY, GMAIL_ENABLE, GMAIL_USERNAME, GMAIL_PASSWORD, GMAIL_PROTO, GMAIL_PATH
import feedparser

def home(request):
    quotes = Quote.objects.all()
    if quotes:
        q = choice(quotes).content
    else:
        q = "Dantalian no Shoka"
    
    most_recent = []
    
    categories = Category.objects.all()
    for category in categories:
        category.bookmarks = []
        for bookmark in category.bookmark_set.all():
            if bookmark.archive == False:
                category.bookmarks.append(bookmark)
    
    if GMAIL_ENABLE:
        newmails = int(feedparser.parse(GMAIL_PROTO+GMAIL_USERNAME+":"+GMAIL_PASSWORD+"@"+GMAIL_PATH)["feed"]["fullcount"])    
    
    sudo = request.session.get('sudo', default = None)
    if sudo == LOGIN_KEY:
        return render_to_response('homepage/private.html', {'quote': q, 'categories': categories, 'newmails': newmails}, context_instance=RequestContext(request))
    else:
        return render_to_response('homepage/public.html', {'quote': q, 'categories': categories}, context_instance=RequestContext(request))