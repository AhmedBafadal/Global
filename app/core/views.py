from rest_framework import viewsets, mixins,  generics,filters
from rest_framework.response import Response
from core.models import Artist, Track
from core import serializers
from rest_framework.renderers import TemplateHTMLRenderer



class CreateTrackViewSet(viewsets.GenericViewSet,
                        mixins.CreateModelMixin):
    """Create New Track"""
    queryset = Track.objects.all()
    serializer_class = serializers.CreateTrackSerializer
    

    def perform_create(self, serializer):
        serializer.save()



class FetchTrackViewSet(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    """Fetch a single track using a track id."""
    
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
    lookup_field = 'track_id'
    
    def get(self, request, track_id=None):
        if track_id:
            return self.retrieve(request, track_id)
        else:
            return Response('Please enter a track id, by appending it in the url field.')

        
class FilterTrackViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin):
    """Filter tracks by name of artist or title of song"""
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'track_id', 'artist__name']
    
class FilterArtistViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin):
    """Filter tracks by name of artist"""
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['artist__name']
    
    def list(self, request):
        print(request.query_params)
        try:
            artists = request.query_params.get('search').split(',')
            artists = [i.strip() for i in artists]
        except Exception as e:
            print(e)
            artists = None
        
        artist_list = []
        if artists:
            for artist in artists:
                query = self.queryset.filter(artist__name=artist)
                total_tracks = len(query)
                last_played = query.order_by('-last_play').first()
                artist_list.append({'Artist': str(artist), 'Total Tracks': int(total_tracks), 'Last Played Track': str(last_played)})

            return Response({"Artists":artist_list})
        return Response("""Please search in the url field, entering multiple artists each seperated by a comma (please append ?search= before entering artist names) example search - /api/filter_artist/?search=Beyonce,Mariah Carey""")
    
    
class LastPlayedTracksViewSet(viewsets.GenericViewSet, 
                              mixins.ListModelMixin):
    """100 most played tracks (most recent first)"""
    queryset = Track.objects.all()
    serializer_class = serializers.TrackSerializer
    
    def get_queryset(self):
        return self.queryset.order_by('-last_play')[:100]
    

    