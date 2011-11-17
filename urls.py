from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'dalian.homepage.views.home'),
    url(r'^ctrlhub/', include('ctrlhub.urls')),
    url(r'^bookmarks/', include('bookmarks.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^notes/', include('notes.urls')),
    url(r'^quotes/add$', 'dalian.quotes.views.add'),
)
