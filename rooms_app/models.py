from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=24, default='')
    description = models.CharField(max_length=256, default='')
    city = models.CharField(max_length=60, default='')
    street = models.CharField(max_length=60, default='')
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)






