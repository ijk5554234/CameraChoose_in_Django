from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'mysite.views.home_page'),
    url(r'^callback/', 'camerachoose.views.compare'),
    url(r'^camerachoose/', include('camerachoose.urls')),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
)
