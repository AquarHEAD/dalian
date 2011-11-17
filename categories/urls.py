from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('categories.views',
    url(r'^add$', 'add'),
    url(r'^manage', 'manage'),
    url(r'^rename/(?P<bookmark_id>\d+)/$', 'rename'),
    url(r'^remove/(?P<bookmark_id>\d+)/$', 'remove'),
)
