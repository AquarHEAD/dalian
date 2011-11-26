from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('dalian.tweets.views',
    url(r'^manage$', 'manage'),
    url(r'^add$','add'),
    url(r'^edit/(?P<tweet_id>\d+)/$', 'edit'),
    url(r'^remove/(?P<tweet_id>\d+)/$', 'remove'),
)
