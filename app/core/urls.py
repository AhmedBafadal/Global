from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register('last_played', views.LastPlayedTracksViewSet, 'last_played')
router.register('filter_track', views.FilterTrackViewSet, 'filter_track')
router.register('add_track', views.CreateTrackViewSet, 'add_track')
router.register('filter_artist', views.FilterArtistViewSet, 'filter_artist')

app_name = 'core'

urlpatterns = [
    path('fetch_track/', views.FetchTrackViewSet.as_view()),
    path('fetch_track/<int:track_id>/', views.FetchTrackViewSet.as_view()),
    path('', include(router.urls))
]

urlpatterns += router.urls
