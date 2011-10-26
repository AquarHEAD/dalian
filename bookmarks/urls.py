from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('bookmarks.views',
    url(r'^manage$', 'manage'),
    url(r'^create-category', 'create_category'),
    url(r'^add-bookmark', 'add_bookmark'),
    url(r'^add-with-cat', 'add_with_cat'),
    url(r'^goto/(?P<bookmark_id>\d+)/$', 'goto'),
    url(r'^edit-bookmark/(?P<bookmark_id>\d+)/$', 'edit_bookmark'),
)
