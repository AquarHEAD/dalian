from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bookmarks.views',
    url(r'^manage$', 'manage'),
    url(r'^add', 'add'),
    url(r'^edit/(?P<bookmark_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<bookmark_id>\d+)/$', 'remove'),
    url(r'^goto/(?P<bookmark_id>\d+)/$', 'goto'),
)
