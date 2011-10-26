from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('ctrlhub.views',
    url(r'^login$', 'login'),
    url(r'^logout$', 'logout'),
    url(r'^main$', 'ctrl_main'),
)
