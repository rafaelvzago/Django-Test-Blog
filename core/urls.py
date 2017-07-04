from django.conf.urls import url
from core.views import home, articles, add, update, delete

urlpatterns = [
    url(r'^$', home),
    url(r'^articles/$', articles, name='articles'),
    url(r'^add/$', add, name='new'),
    url(r'^update/(?P<id>\d+)/$', update, name='update'),
    url(r'^delete/(?P<id>\d+)/$', delete, name='delete'),
]
