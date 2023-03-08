from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=24)
    description = models.CharField(max_length=256)
    city = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    street_number = models.CharField(max_length=12)
    local_number = models.IntegerField()
    post_code_first = models.IntegerField()
    post_code_second = models.IntegerField()
    level = models.IntegerField(default=0)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=None)
    seats = models.IntegerField()
    tables = models.BooleanField(default=None)
    catering = models.BooleanField(default=None)
    private_parking = models.BooleanField(default=None)
    sound_system = models.BooleanField(default=None)


