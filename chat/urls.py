from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^connect', 'app.views.connect', name='connect'),
    url(r'^check', 'app.views.checkmessages', name='checkmessages'),
    url(r'^count', 'app.views.get_total_user', name='get_total_user'),
    url(r'^stop', 'app.views.stopsearch', name='stopsearch'),
    url(r'^send', 'app.views.sendmessage', name='sendmessage'),
    url(r'^admin/', include(admin.site.urls)),
]
