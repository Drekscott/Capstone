from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'portfolio.views.my_portfolios'),
    url(r'^get/(?P<portfolio_id>\d+)/$', 'portfolio.views.my_portfolio'),
    url(r'^like/(?P<portfolio_id>\d+)/$', 'portfolio.views.like_portfolio'),

)
