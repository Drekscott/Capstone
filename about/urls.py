from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
url (r'^all/$', 'about.views.about_me'),
url(r'^get/(?P<about_id>\d+)/$', 'about.views.About'),

)
