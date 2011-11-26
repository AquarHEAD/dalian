from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dalian.categories.views',
    url(r'^add$', 'add'),
    url(r'^manage', 'manage'),
    url(r'^rename/(?P<category_id>\d+)/$', 'rename'),
    url(r'^remove/(?P<category_id>\d+)/$', 'remove'),
)
