from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^$', 'dalian.homepage.views.home'),
    url(r'^login$', 'dalian.ctrlhub.views.login'),
    url(r'^logout$', 'dalian.ctrlhub.views.logout'),
    url(r'^ctrlhub$', 'dalian.ctrlhub.views.ctrl_main'),
    url(r'^quotes/add$', 'dalian.quotes.views.add'),
    url(r'^bookmarks/create-category', 'dalian.bookmarks.views.create_category'),
    url(r'^bookmarks/add-bookmark', 'dalian.bookmarks.views.add_bookmark'),
    url(r'^bookmarks/add-with-cat', 'dalian.bookmarks.views.add_with_cat'),
    url(r'^bookmarks/goto/(?P<bookmark_id>\d+)/$', 'dalian.bookmarks.views.goto'),
    # Examples:
    # url(r'^$', 'dalian.views.home', name='home'),
    # url(r'^dalian/', include('dalian.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
