from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^toto/', include('toto.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

URL_ROOT = 'portal'
urlpatterns += patterns('apps.portal.views',
    url(r'home/$', 'home', name='%s_home' % URL_ROOT),
)

# Serve static files through Django only if we are in a debug environment
# because it is not secure at all. Also, activate admin only in DEBUG mode.
if settings.DEBUG == True:
    urlpatterns += patterns('',
        (r'^admin/', include(admin.site.urls)),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )
