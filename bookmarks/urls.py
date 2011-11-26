from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dalian.bookmarks.views',
    url(r'^manage$', 'manage'),
    url(r'^add$', 'add'),
    url(r'^add-with-cat$', 'add_with_cat'),
    url(r'^edit/(?P<bookmark_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<bookmark_id>\d+)/$', 'remove'),
    url(r'^goto/(?P<bookmark_id>\d+)/$', 'goto'),
)
