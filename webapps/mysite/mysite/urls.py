from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # polls application
    url(r'^polls/', include('polls.urls', namespace='polls')),
    # blog application
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # gallery application
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
  urlpatterns += patterns('django.views.static',
    (r'media/(?P<path>.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
    (r'static/(?P<path>.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
  )
