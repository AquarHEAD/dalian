from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from random import choice
from dalian.bookmarks.models import Category
from dalian.quotes.models import Quote

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
    
    sudo = request.session.get('sudo', default = None)
    if sudo == 'dalian':
        return private(request, q, categories)
    else:
        return public(request, q, categories)

def public(request, q, categories):
    
    return render_to_response('homepage/public.html', {'quote': q, 'categories': categories}, context_instance=RequestContext(request))
    
def private(request, q, categories):
    
    return render_to_response('homepage/private.html', {'quote': q, 'categories': categories}, context_instance=RequestContext(request))