from django.db import models
from django.db.models.signals import pre_save
from .utils import artiste_id_generator, song_id_generator
from django.contrib.auth.models import User

#As you might have guessed, there is a relationship between all three Models.
#An Artiste can have multiple songs, and a song can have multiple lyrics.
# A song must only belong to one Artiste and a lyric must only belong to a song. 
#You are to specify the foreignkey relationship yourself.
#Also, the model field attributes should be specified by you. 

#Push the task to GitHub when you finish and submit the GitHub repository link

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    age = models.IntegerField(null=True, blank=True)
    artiste_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '%s %s - %s' % (self.first_name, self.last_name, self.artiste_id)


class Song(models.Model):
    title = models.CharField(max_length = 50)
    date_released = models.DateField()
    likes = models.ManyToManyField(User, related_name='song', blank=True, default=None)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE, related_name="Artiste_ids", null=True)
    song_id = models.CharField(max_length=50, blank=True)
    

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return '%s | %s' % (self.title, self.song_id)


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE, related_name="song_ids", null=True)


    def __str__(self):
        return str(self.song_id.title)




def pre_save_artiste_id(sender, instance, *args, **kwargs):
        if not instance.artiste_id:
            instance.artiste_id = artiste_id_generator(instance)
    
pre_save.connect(pre_save_artiste_id, sender=Artiste)
    

def pre_save_song_id(sender, instance, *args, **kwargs):
        if not instance.song_id:
            instance.song_id = song_id_generator(instance)
    
pre_save.connect(pre_save_song_id, sender=Song)


