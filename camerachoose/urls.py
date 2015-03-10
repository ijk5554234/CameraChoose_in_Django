__author__ = 'Jike'
from django.conf.urls import patterns, include, url
import mysite
urlpatterns = patterns('',
    url(r'^login/', 'camerachoose.views.login'),
    url(r'^investigate/', 'camerachoose.views.investigate'),
    url(r'^templay/', 'camerachoose.views.list'),
    url(r'^index/', 'camerachoose.views.index'),
    url(r'^compare/', 'camerachoose.views.compare'),
    url(r'^test/', 'camerachoose.views.test'),
    url(r'^result/', 'camerachoose.views.result'),
    url(r'^anothertest/', 'camerachoose.views.anothertest'),
    url(r'^logout/', 'camerachoose.views.logout'),
    url(r'^$', 'camerachoose.views.index'),

    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': mysite.settings.STATICFILES_DIRS, 'show_indexes': True}),
)
