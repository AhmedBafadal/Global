from core.models import Track, Artist
from marshmallow import Schema, fields, post_load
import json
import logging
from multiprocessing import Process


class TrackSchema(Schema):
    """Serialize the json data."""
    id = fields.Int()
    title = fields.Str()
    artist = fields.Str()
    duration = fields.Decimal()
    last_play = fields.DateTime()
    
    @post_load
    def create_track(self, data,**kwargs):
        artist, created = Artist.objects.get_or_create(name=data['artist'].strip())
        track = Track(track_id= data['id'], title= data['title'], artist= artist,duration= data['duration'], last_play= data['last_play'])
        track.save()


        
def run():
    """Run script to save tracks.json data to the database."""
    logger = logging.getLogger(__name__)
    logger.info('LOADING DATA....')
    Track.objects.all().delete()
    Artist.objects.all().delete()
    
    with open('scripts/tracks.json','r') as f:
        raw_data = f.read()
    

    track_schema = TrackSchema()
    try:
        track_schema.loads(raw_data, many=True)
    except Exception as e:
        with open('error.txt', 'a') as f1:
            f1.write(str({"Error":e}))
            f1.write('\n')
            f1.write('-----')
            f1.write('\n')
            logging.error(e)

    logger.info('LOAD DATA COMPLETE!')
    
    
    

    