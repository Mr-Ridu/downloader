from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('' ,views.downloadyt, name="downloadyt"),
    path('ytdetails' , views.ytdetails, name="ytdetails"),
    path('playlistshow' , views.playlistshow, name="playlistshow"),
    path('newdown/<itag>/' , views.newdown, name="newdown"),
    path('playlist_download/', views.playlist_download, name='playlist_download')
]