from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('notes.views',
    url(r'^home$', 'home'),
    url(r'^add$', 'add'),
    url(r'^edit/(?P<note_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<note_id>\d+)/$', 'remove'),
    url(r'^view/(?P<note_id>\d+)/$', 'view'),
)
