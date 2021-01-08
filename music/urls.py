from django.conf.urls import url
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
admin.autodiscover()

app_name = 'music'

urlpatterns = [
    url(r'^result/$',views.Search.as_view(),name='result'),


    url(r'^contact/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)/$',views.contact,name='contact'),

    url(r'^login/$', auth_views.login,{'template_name': 'music/login.html'},name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': '/music'}, name='logout'),
    url(r'^admin/', admin.site.urls),

    #/musicaaaaaaa/
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^mine/$',views.Mine.as_view(), name='mine'),

    url(r'^register/$', views.UserFormView.as_view(),name='register'),

    url(r'^signup/$',views.SignUpView,name='signup'),

    #/music/71/ group tells they are one item
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #/music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),

    # /music/station/add/
    url(r'station/add/$', views.StationCreate.as_view(), name='station-add'),

    url(r'station/(?P<pk>[0-9]+)/$', views.StationUpdate.as_view(), name='station-update'),

    url(r'station/(?P<pk>[0-9]+)/delete/$', views.StationDelete.as_view(), name='station-delete'),


]