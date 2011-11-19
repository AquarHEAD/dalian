from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('notes.views',
    url(r'^manage$', 'manage'),
    url(r'^add$', 'add'),
    url(r'^edit/(?P<note_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<note_id>\d+)/$', 'remove'),
)
