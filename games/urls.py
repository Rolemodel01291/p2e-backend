from django.conf.urls import url 
from games import views
 
urlpatterns = [ 
    url(r'^api/games/page/(?P<page>[1-9]+)$', views.list),
    url(r'^api/games/filter/(?P<platform>[\w\-]+)/(?P<genre>[\w\-]+)/(?P<device>[\w\-]+)/(?P<status>[\w\-]+)/(?P<nft>[\w\-]+)/(?P<f2p>[\w\-]+)/(?P<p2e>[\w\-]+)$', views.filter),
    url(r'^api/games/search/(?P<keyword>[\w\-]+)$', views.search),
    url(r'^api/games/new$', views.new_list),
    url(r'^api/games/autocomplete/(?P<keyword>[\w\-]+)$', views.auto_complete),
    url(r'^api/game/(?P<id>[0-9]+)$', views.detail),
    url(r'^api/game/(?P<id>[0-9]+)/history$', views.history),
    url(r'^api/game/(?P<id>[0-9]+)/contracts$', views.contracts),
]