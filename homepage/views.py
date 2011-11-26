from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from random import choice
from dalian.categories.models import Category
from dalian.quotes.models import Quote
from dalian.utils.decorators import login_check
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
        category.count = 0
        category.has_archived = False;
        for bookmark in category.bookmark_set.all():
            if bookmark.archive == False:
                category.count += 1
            else:
                category.has_archived = True
            category.bookmarks.append(bookmark)
    
    sudo = request.session.get('sudo', default = None)
    if sudo == LOGIN_KEY:
        return render_to_response('homepage/private.html', {'quote': q, 'categories': categories, 'gmail_enable': GMAIL_ENABLE}, context_instance=RequestContext(request))
    else:
        return render_to_response('homepage/public.html', {'quote': q, 'categories': categories}, context_instance=RequestContext(request))
        
@login_check(LOGIN_KEY)
def gmail_count(request):
    gc = int(feedparser.parse(GMAIL_PROTO+GMAIL_USERNAME+":"+GMAIL_PASSWORD+"@"+GMAIL_PATH)["feed"]["fullcount"])
    return HttpResponse(gc)