from rest_framework import serializers
from core.models import Artist, Track

class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for Artist objects"""
    
    class Meta:
        model = Artist
        fields = ('name',)
        
class TrackSerializer(serializers.ModelSerializer):
    """Serializer for Track objects"""
    artist_name = serializers.CharField(source='artist.name')
    
    class Meta:
        model = Track
        fields = ('track_id', 'title', 'artist_name', 'duration','last_play')    
        

class CreateTrackSerializer(TrackSerializer):
    """Serializer for Creating Track objects"""
    artist_id = serializers.PrimaryKeyRelatedField(source='artist',
                                                   queryset=Artist.objects.all())
    
    class Meta:
        model = Track
        fields = ('track_id', 'title', 'artist_id', 'duration','last_play')

