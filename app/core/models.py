from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Track(models.Model):
    track_id = models.IntegerField(unique=True, null=True)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    duration = models.DecimalField(max_digits=8,decimal_places=2)
    last_play = models.DateTimeField()
    
    def __str__(self):
        return self.title
    


