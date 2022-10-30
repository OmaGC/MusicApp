import random 
import string
from django.utils.text import slugify


def random_id_generator(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def artiste_id_generator(instance):
    new_artiste_id = random_id_generator()

    value = instance.__class__
    id_exists = value.objects.filter(artiste_id=new_artiste_id).exists()

    if id_exists:
        return artiste_id_generator(instance)
    return new_artiste_id



def song_id_generator(instance):
    new_song_id = random_id_generator()

    value = instance.__class__
    id_exists = value.objects.filter(song_id=new_song_id).exists()

    if id_exists:
        return song_id_generator(instance)
    return new_song_id