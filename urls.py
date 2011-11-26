from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dalian.homepage.views.home'),
    url(r'^gc$', 'dalian.homepage.views.gmail_count'),
    url(r'^ctrlhub/', include('dalian.ctrlhub.urls')),
    url(r'^bookmarks/', include('dalian.bookmarks.urls')),
    url(r'^categories/', include('dalian.categories.urls')),
    url(r'^notes/', include('dalian.notes.urls')),
    url(r'^tweets/',include('dalian.tweets.urls')),
    url(r'^quotes/add$', 'dalian.quotes.views.add'),
)
